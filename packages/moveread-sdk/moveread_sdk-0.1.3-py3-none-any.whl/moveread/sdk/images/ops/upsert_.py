from typing import Callable, NamedTuple
import asyncio
import haskellian.either as E
from moveread.core import Game, SheetID, ImageID, Image, CoreAPI
from moveread.errors import InexistentGame, InexistentPlayer, InexistentSheet, InexistentImage, DBError, InexistentItem, InvalidData
from moveread.sdk.util.blobs import image_url

class InsertOk(NamedTuple):
  game: Game
  url: str

def upsert_url(
  game: Game, id: SheetID, meta, *,
  img_url: Callable[[ImageID], str] | None = None,
  version: int | None = None
) -> E.Either[InexistentPlayer|InexistentSheet|InexistentImage, InsertOk]:
  """Insert Image to sheet. Appends if `version is None`"""

  img_url = img_url or image_url

  game = game.model_copy()

  if len(game.players) <= id.player:
    return E.Left(InexistentPlayer(id, num_players=len(game.players)))
  
  player = game.players[id.player]
  if len(player.sheets) <= id.page:
    return E.Left(InexistentSheet(id, num_pages=len(player.sheets)))
  
  sheet = player.sheets[id.page]

  if version is None:
    url = img_url(id.imageId(version=len(sheet.images)))
    sheet.images.append(Image(url=url, meta=meta))
    return E.Right(InsertOk(game, url))
  
  elif version < len(sheet.images):
    url = img_url(id.imageId(version))
    sheet.images[version] = Image(url=url, meta=meta)
    return E.Right(InsertOk(game, url))
  
  else:
    return E.Left(InexistentImage(id.imageId(version), num_versions=len(sheet.images)))
  
async def upsert(
  id: SheetID, img: bytes, meta, *,
  api: CoreAPI, version: int | None = None,
  img_url: Callable[[ImageID], str] | None = None
) -> E.Either[InexistentGame|InexistentSheet|InexistentPlayer|InvalidData|DBError, Game]:
  try:
    game = (await api.games.read(id.gameId)).unsafe()
    new_game, url = upsert_url(game, id, meta=meta, img_url=img_url, version=version).unsafe()
    results = await asyncio.gather(
      api.games.update(id.gameId, new_game),
      api.blobs.insert(url, img, replace=True),
    )
    return E.sequence(results).mapl(lambda errs: DBError(errs)).fmap(lambda _: new_game)
  except E.IsLeft as e:
    if isinstance(e.value, InexistentItem):
      return E.Left(InexistentGame(id.gameId, e.value))
    return E.Left(e.value)
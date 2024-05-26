from typing import NamedTuple, Callable
import asyncio
import haskellian.either as E
from haskellian.iter import flatten
from moveread.core import CoreAPI, Game, Player, Sheet, Image, ImageID
from moveread.errors import DBError
from ...util import image_url

class NewGame(NamedTuple):
  game: Game
  blobs: list[tuple[str, bytes]]

def make(gameId: str, imgs: list[list[bytes]], *, img_url: Callable[[ImageID], str] | None = None) -> NewGame:
  """New Game data"""
  img_url = img_url or image_url
  blobs = [
    [(img_url(ImageID(gameId, player, page)), img) for page, img in enumerate(player_imgs)]
    for player, player_imgs in enumerate(imgs)
  ]
  players = [
    Player(sheets=[Sheet(images=[Image(url=url)]) for url, _ in player_urls])
    for player_urls in blobs
  ]
  game = Game(id=gameId, players=players)
  return NewGame(game, list(flatten(blobs)))

async def create(
  gameId: str, imgs: list[list[bytes]], *,
  replace = False, api: CoreAPI, img_url: Callable[[ImageID], str] | None = None
) -> E.Either[DBError, Game]:
  """Transactionally create a game"""
  game, blobs = make(gameId, imgs, img_url=img_url)
  tasks = [
    api.games.insert(gameId, game),
    *[api.blobs.insert(url, img) for url, img in blobs]
  ]
  results = await asyncio.gather(*tasks)
  end_result = await E.sequence(results).match_(api.rollback, api.commit)
  return E.sequence([*results, end_result]).mapl(
    lambda errs: DBError(errs)
  ).fmap(
    lambda _: game
  )
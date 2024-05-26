import haskellian.either as E
from moveread.core import CoreAPI, Game, ImageID
from moveread.annotations.images import ImageMeta
from moveread.errors import DBError, InvalidData, InexistentPlayer, InexistentGame, InexistentSheet, InexistentImage, InexistentItem

async def annotate(
  id: ImageID, meta: ImageMeta, *, api: CoreAPI
) -> E.Either[InexistentGame|InvalidData|InexistentPlayer|InexistentSheet|InexistentImage|DBError, Game]:
   try:
      game = (await api.games.read(id.gameId)).unsafe()

      if id.player >= len(game.players):
         return E.Left(InexistentPlayer(playerId=id, num_players=len(game.players)))
      
      player = game.players[id.player]
      if id.page >= len(player.sheets):
         return E.Left(InexistentSheet(sheetId=id, num_pages=len(player.sheets)))

      sheet = player.sheets[id.page]
      if id.version >= len(sheet.images):
         return E.Left(InexistentImage(imageId=id, num_versions=len(player.sheets)))

      image = sheet.images[id.version]
      image.meta = (image.meta or {}) | meta.model_dump(exclude_none=True)
      (await api.games.update(id.gameId, game)).unsafe()
      return E.Right(game)
   except E.IsLeft as e:
      if isinstance(e, InexistentItem):
         return E.Left(InexistentGame(id.gameId, e.value))
      return E.Left(e.value)
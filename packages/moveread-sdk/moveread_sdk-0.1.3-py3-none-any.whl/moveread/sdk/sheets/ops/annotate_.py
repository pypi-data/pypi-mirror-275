import haskellian.either as E
from moveread.core import CoreAPI, Game, SheetID
from moveread.annotations.sheets import SheetMeta
from moveread.errors import DBError, InvalidData, InexistentPlayer, InexistentGame, InexistentSheet, InexistentItem

async def annotate(
  id: SheetID, meta: SheetMeta, *, api: CoreAPI
) -> E.Either[InvalidData|InexistentGame|InexistentPlayer|InexistentSheet|DBError, Game]:
   try:
      game = (await api.games.read(id.gameId)).unsafe()

      if id.player >= len(game.players):
         return E.Left(InexistentPlayer(playerId=id, num_players=len(game.players)))
      
      player = game.players[id.player]
      if id.page >= len(player.sheets):
         return E.Left(InexistentSheet(sheetId=id, num_pages=len(player.sheets)))

      sheet = player.sheets[id.page]
      sheet.meta = (sheet.meta or {}) | meta.model_dump(exclude_none=True)
      (await api.games.update(id.gameId, game)).unsafe()
      return E.Right(game)
   except E.IsLeft as e:
      if isinstance(e, InexistentItem):
         return E.Left(InexistentGame(id.gameId, e.value))
      return E.Left(e.value)
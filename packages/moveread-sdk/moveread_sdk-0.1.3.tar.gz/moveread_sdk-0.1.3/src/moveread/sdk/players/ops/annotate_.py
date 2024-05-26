import haskellian.either as E
from moveread.core import CoreAPI, Game, PlayerID
from moveread.annotations.players import PlayerMeta
from moveread.errors import DBError, InvalidData, InexistentPlayer, InexistentGame, InexistentItem

async def annotate(id: PlayerID, meta: PlayerMeta, *, api: CoreAPI) -> E.Either[InvalidData|InexistentGame|InexistentPlayer|DBError, Game]:
   try:
      game = (await api.games.read(id.gameId)).unsafe()

      if id.player >= len(game.players):
         return E.Left(InexistentPlayer(playerId=id, num_players=len(game.players)))
      
      player = game.players[id.player]
      player.meta = (player.meta or {}) | meta.model_dump(exclude_none=True)
      (await api.games.update(id.gameId, game)).unsafe()
      return E.Right(game)
   except E.IsLeft as e:
      if isinstance(e.value, InexistentItem):
         return E.Left(InexistentGame(id.gameId, e.value))
      return E.Left(e.value)
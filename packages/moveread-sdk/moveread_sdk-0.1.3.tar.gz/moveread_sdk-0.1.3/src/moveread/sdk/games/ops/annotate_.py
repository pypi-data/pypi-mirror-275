import haskellian.either as E
from moveread.core import CoreAPI, Game
from moveread.annotations import GameMeta
from moveread.errors import DBError, InvalidData, InexistentItem, InexistentGame

async def annotate(gameId: str, meta: GameMeta, *, api: CoreAPI) -> E.Either[InexistentGame|InvalidData|DBError, Game]:
   try:
      game = (await api.games.read(gameId)).unsafe()
      game.meta = (game.meta or {}) | meta.model_dump(exclude_none=True)
      (await api.games.update(gameId, game)).unsafe()
      return E.Right(game)
   except E.IsLeft as e:
      if isinstance(e.value, InexistentItem):
         return E.Left(InexistentGame(gameId, e.value))
      return E.Left(e.value)
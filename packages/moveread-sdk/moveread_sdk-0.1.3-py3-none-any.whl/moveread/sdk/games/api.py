from moveread.core import CoreAPI
from . import ops

class GamesAPI:

  def __init__(self, core: CoreAPI) -> None:
    self._core = core

  async def create(self, gameId: str, imgs: list[list[bytes]], *, replace: bool = False):
    return await ops.create(gameId, imgs, replace=replace, api=self._core)
  
  async def read(self, gameId: str):
    return await self._core.games.read(gameId)
  
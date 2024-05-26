from moveread.core import CoreAPI, PlayerID
from . import ops

class PlayersAPI:

  def __init__(self, core: CoreAPI):
    self._core = core

  async def annotate(self, id: PlayerID, schema: str, meta):
    return await ops.annotate(id, schema, meta, api=self._core)
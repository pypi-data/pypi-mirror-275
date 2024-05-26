from moveread.core import CoreAPI, SheetID
from . import ops

class SheetsAPI:

  def __init__(self, core: CoreAPI):
    self._core = core

  async def annotate(self, id: SheetID, schema: str, meta):
    return await ops.annotate(id, schema, meta, api=self._core)
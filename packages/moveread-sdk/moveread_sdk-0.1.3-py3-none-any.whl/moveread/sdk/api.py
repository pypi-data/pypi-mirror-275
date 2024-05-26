from moveread.core import CoreAPI
from .games import GamesAPI
from .players import PlayersAPI
from .sheets import SheetsAPI
from .images import ImagesAPI

class MovereadAPI:

  @classmethod
  def at(cls, path: str, blobs_extension: str = '.jpg') -> 'MovereadAPI':
    try:
      core = CoreAPI.at(path, blobs_extension=blobs_extension)
      return cls(core)
    except ImportError as e:
      e.add_note('Install `moveread.local` or `moveread.sdk[local]` to create a local API')
      raise e
  
  @classmethod
  def debug(cls, path: str, blobs_extension: str = '.jpg') -> 'MovereadAPI':
    try:
      core = CoreAPI.debug(path, blobs_extension=blobs_extension)
      return cls(core)
    except ImportError as e:
      e.add_note('Install `moveread.local` or `moveread.sdk[local]` to create a local API')
      raise e

  def __init__(self, core: CoreAPI):
    self.core = core
    self.games = GamesAPI(core)
    self.players = PlayersAPI(core)
    self.sheets = SheetsAPI(core)
    self.images = ImagesAPI(core)
    
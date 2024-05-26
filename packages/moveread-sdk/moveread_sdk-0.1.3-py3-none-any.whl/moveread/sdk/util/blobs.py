from moveread.core import ImageID

def image_url(id: ImageID):
  return f'{id.gameId}/{id.player}-{id.page}-{id.version}'
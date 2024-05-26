# Moveread SDK

> Python SDK for the Moveread Core

## Usage

- Local API (install with `pip install moveread-sdk[local]`)

```python
from moveread.sdk import MovereadAPI

api = MovereadAPI.at('path/to/data')
await api.games.create('new-game', [[b'img1'], [b'img2']])

await api.images.annotate(...)
```

- Any API

```python
from moveread.core import CoreAPI
from moveread.sdk import MovereadAPI

class CustomAPI(CoreAPI):
  ...

api = MovereadAPI(CustomAPI())
```
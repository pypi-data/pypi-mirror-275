from typing import Literal, Any
from dataclasses import dataclass
from moveread.core.ids import PlayerID, SheetID, ImageID

@dataclass
class InexistentGame(BaseException):
  gameId: str
  detail: Any = None
  reason: Literal['inexistent-game'] = 'inexistent-game'


@dataclass
class InexistentPlayer(BaseException):
  playerId: PlayerID
  num_players: int
  detail: Any = None
  reason: Literal['inexistent-player'] = 'inexistent-player'

@dataclass
class InexistentSheet(BaseException):
  sheetId: SheetID
  num_pages: int
  detail: Any = None
  reason: Literal['inexistent-sheet'] = 'inexistent-sheet'

@dataclass
class InexistentImage(BaseException):
  imageId: ImageID
  num_versions: int
  detail: Any = None
  reason: Literal['inexistent-image'] = 'inexistent-image'
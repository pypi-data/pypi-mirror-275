from typing import Literal, Any
from dataclasses import dataclass
from .db import InvalidData

@dataclass
class MissingMeta(BaseException):
  detail: Any
  reason: Literal['missing-metadata'] = 'missing-metadata'
  
@dataclass
class InexistentSchema(BaseException):
  schema: str
  detail: Any
  reason: Literal['inexistent-schema'] = 'inexistent-schema'

InvalidMeta = InexistentSchema | InvalidData
from pydantic import BaseModel
from typing import TypeVar

BM = TypeVar('BM', bound=BaseModel)
T = TypeVar('T', bound=BaseModel)

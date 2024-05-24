from typing import TypeVar

from pydantic import BaseModel

BM = TypeVar("BM", bound=BaseModel)

T = TypeVar("T", bound=BaseModel)

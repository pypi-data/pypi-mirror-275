from .types import BM
from pydantic import BaseModel
from typing import Generic

__all__ = ['Pagination', 'AggregatePag']

class Pagination(BaseModel, Generic[BM]):
    data: list[BM]
    pages: int
    total: int

class AggregatePag(BaseModel, Generic[BM]):
    total: int
    data: list[BM]

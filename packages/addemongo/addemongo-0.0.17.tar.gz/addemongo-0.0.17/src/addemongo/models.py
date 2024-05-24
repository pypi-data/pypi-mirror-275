__all__ = ("Pagination", "AggregatePag")

from typing import Generic

from pydantic import BaseModel

from .types import BM


class Pagination(BaseModel, Generic[BM]):
    data: list[BM]
    pages: int
    total: int


class AggregatePag(BaseModel, Generic[BM]):
    total: int
    data: list[BM]

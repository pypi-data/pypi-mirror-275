from .main import MongoConnection as MongoConnection
from .types import BM as BM
from _typeshed import Incomplete
from typing import Any, Generic

class MongoBaseClient(Generic[BM]):
    connection: Incomplete
    database_name: Incomplete
    collection_name: Incomplete
    response_class: Incomplete
    def __init__(self, connection: MongoConnection, database: str, collection: str, response_class: type[BM]) -> None: ...
    def projection_schema(self) -> dict[str, Any]: ...

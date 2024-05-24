from math import ceil
from typing import TYPE_CHECKING, Any, Mapping, Optional, Sequence, Type, Union

from motor.motor_asyncio import AsyncIOMotorClient as _MotorAsyncIOClient
from pymongo import MongoClient as _PyMongoClient

from ._base_client import MongoBaseClient
from .builders import AggregationBuilder, QueryBuilder
from .models import AggregatePag, Pagination
from .types import BM, T

if TYPE_CHECKING:
    from motor.motor_asyncio import AsyncIOMotorCollection as _AsyncIOMotorCollection
    from motor.motor_asyncio import AsyncIOMotorDatabase as _AsyncIOMotorDatabase
    from pymongo.collection import Collection as _PyMongoCollection
    from pymongo.database import Database as _PyMongoDatabase
    from pymongo.results import (
        DeleteResult,
        InsertManyResult,
        InsertOneResult,
        UpdateResult,
    )


class MongoConnection:
    def __init__(
        self,
        host: Optional[Union[str, Sequence[str]]],
        port: Optional[int] = None,
        tz_aware: Optional[bool] = None,
        connect: Optional[bool] = None,
        **kwargs: Any,
    ) -> None:
        self.host = host
        self.port = port
        self.tz_aware = tz_aware
        self.connect = connect
        self.kwargs = kwargs

    def async_client(
        self, database_name: str, collection_name: str, model: type[BM]
    ) -> "MongoAsyncClient[BM]":
        """
        Async client made with the motor package used to interact with the database
        """
        return MongoAsyncClient[BM](
            connection=self,
            database=database_name,
            collection=collection_name,
            response_class=model,
        )

    def sync_client(
        self, database_name: str, collection_name: str, model: type[BM]
    ) -> "MongoSyncClient[BM]":
        return MongoSyncClient[BM](
            connection=self,
            database=database_name,
            collection=collection_name,
            response_class=model,
        )


class MongoSyncClient(MongoBaseClient[BM]):
    def __init__(
        self,
        connection: "MongoConnection",
        database: str,
        collection: str,
        response_class: Type[BM],
    ) -> None:
        self.connection = connection
        self.database_name = database
        self.collection_name = collection
        self.response_class = response_class
        self.client: _PyMongoClient[Mapping[str, Any]] = _PyMongoClient(
            host=self.connection.host,
            port=self.connection.port,
            tz_aware=self.connection.tz_aware,
            connect=self.connection.connect,
            **self.connection.kwargs,
        )
        self.database: "_PyMongoDatabase[Any]" = self.client[self.database_name]
        self.collection: "_PyMongoCollection[Any]" = self.database[self.collection_name]

    def insert_one(self, document: BM) -> "InsertOneResult":
        return self.collection.insert_one(document.model_dump())

    def insert_many(self, documents: list[BM]) -> "InsertManyResult":
        return self.collection.insert_many(
            [document.model_dump() for document in documents]
        )

    def update_one(
        self, query: QueryBuilder, document: BM, upsert: bool = False
    ) -> "UpdateResult":
        return self.collection.update_one(
            filter=query.build(), update={"$set": document.model_dump()}, upsert=upsert
        )

    def update_many(
        self, document: BM, query: QueryBuilder = QueryBuilder(), upsert: bool = False
    ) -> "UpdateResult":
        return self.collection.update_many(
            filter=query.build(), update={"$set": document.model_dump()}, upsert=upsert
        )

    def find_one(self, query: QueryBuilder) -> Optional[BM]:
        if document := self.collection.find_one(
            query.build(), projection=self.projection_schema()
        ):
            return self.response_class(**document)
        return None

    def find_many(
        self, query: QueryBuilder = QueryBuilder(), limit: int = 0, skip: int = 0
    ) -> list[BM]:
        return [
            self.response_class(**document)
            for document in self.collection.find(
                query.build(),
                projection=self.projection_schema(),
                limit=limit,
                skip=skip,
            )
        ]

    def pagination(
        self, query: QueryBuilder = QueryBuilder(), page: int = 0, per_page: int = 10
    ) -> Pagination[BM]:
        count = self.count_documents(query)
        docs = self.find_many(query, limit=per_page, skip=page * per_page)

        return Pagination[BM](pages=ceil(count // per_page), total=count, data=docs)

    def delete_one(self, query: QueryBuilder) -> "DeleteResult":
        return self.collection.delete_one(query.build())

    def delete_many(self, query: QueryBuilder = QueryBuilder()) -> "DeleteResult":
        return self.collection.delete_many(query.build())

    def count_documents(self, query: QueryBuilder = QueryBuilder()) -> int:
        return self.collection.count_documents(query.build())

    def aggregation(
        self,
        document_class: type[T],
        pipeline: AggregationBuilder = AggregationBuilder(),
    ) -> list[T]:
        self.collection.aggregate(pipeline=pipeline.build())
        return [
            document_class(**document)
            for document in self.collection.aggregate(pipeline=pipeline.build())
        ]

    def aggregation_pagination(
        self,
        document_class: type[T],
        pipeline: AggregationBuilder = AggregationBuilder(),
        page: int = 0,
        per_page: int = 10,
    ) -> Pagination[T]:
        raw_data = self.collection.aggregate(
            pipeline.set_facet(
                {
                    "total": [{"$count": "total"}],
                    "data": [{"$skip": page * per_page}, {"$limit": per_page}],
                }
            ).build()
        )

        for sla in raw_data:
            data = sla
            docs: AggregatePag[T] = AggregatePag(**data)
            break

        else:
            return Pagination[T](pages=0, total=0, data=[])

        return Pagination[T](
            pages=ceil(docs.total // per_page), total=docs.total, data=docs.data
        )


class MongoAsyncClient(MongoBaseClient[BM]):
    def __init__(
        self,
        connection: "MongoConnection",
        database: str,
        collection: str,
        response_class: Type[BM],
    ) -> None:
        self.connection = connection
        self.database_name = database
        self.collection_name = collection
        self.response_class = response_class
        self.client: _MotorAsyncIOClient = _MotorAsyncIOClient(
            host=self.connection.host,
            port=self.connection.port,
            tz_aware=self.connection.tz_aware,
            connect=self.connection.connect,
            **self.connection.kwargs,
        )
        self.database: _AsyncIOMotorDatabase = self.client[self.database_name]
        self.collection: _AsyncIOMotorCollection = self.database[self.collection_name]

    async def insert_one(self, document: BM) -> "InsertOneResult":
        return await self.collection.insert_one(document.model_dump())

    async def insert_many(self, documents: list[BM]) -> "InsertManyResult":
        return await self.collection.insert_many(
            [document.model_dump() for document in documents]
        )

    async def update_one(
        self, query: QueryBuilder, document: BM, upsert: bool = False
    ) -> "UpdateResult":
        return await self.collection.update_one(
            filter=query.build(), update={"$set": document.model_dump()}, upsert=upsert
        )

    async def update_many(
        self, document: BM, query: QueryBuilder = QueryBuilder(), upsert: bool = False
    ) -> "UpdateResult":
        return await self.collection.update_many(
            filter=query.build(), update={"$set": document.model_dump()}, upsert=upsert
        )

    async def find_one(self, query: QueryBuilder) -> Optional[BM]:
        if document := await self.collection.find_one(
            query.build(), projection=self.projection_schema()
        ):
            return self.response_class(**document)
        return None

    async def find_many(
        self, query: QueryBuilder = QueryBuilder(), limit: int = 0, skip: int = 0
    ) -> list[BM]:
        return [
            self.response_class(**document)
            for document in await self.collection.find(
                query.build(),
                projection=self.projection_schema(),
                limit=limit,
                skip=skip,
            ).to_list(length=None)
        ]

    async def delete_one(self, query: QueryBuilder) -> "DeleteResult":
        return await self.collection.delete_one(query.build())

    async def delete_many(self, query: QueryBuilder = QueryBuilder()) -> "DeleteResult":
        return await self.collection.delete_many(query.build())

    async def count_documents(self, query: QueryBuilder = QueryBuilder()) -> int:
        return await self.collection.count_documents(query.build())

    async def aggregation(
        self,
        document_class: type[T],
        pipeline: AggregationBuilder = AggregationBuilder(),
    ) -> list[T]:
        return [
            document_class(**document)
            for document in await self.collection.aggregate(
                pipeline=pipeline.build()
            ).to_list(length=None)
        ]

    async def pagination(
        self, query: QueryBuilder = QueryBuilder(), page: int = 0, per_page: int = 10
    ) -> Pagination[BM]:
        count = await self.count_documents(query)
        docs = await self.find_many(query, limit=per_page, skip=page * per_page)

        return Pagination[BM](pages=ceil(count // per_page), total=count, data=docs)

    async def aggregation_pagination(
        self,
        document_class: type[T],
        pipeline: AggregationBuilder = AggregationBuilder(),
        page: int = 0,
        per_page: int = 10,
    ) -> Pagination[T]:
        raw_data = self.collection.aggregate(
            pipeline.set_facet(
                {
                    "total": [{"$count": "total"}],
                    "data": [{"$skip": page * per_page}, {"$limit": per_page}],
                }
            ).build()
        )

        async for data in raw_data:
            docs: AggregatePag[T] = AggregatePag(**data)
            break

        else:
            return Pagination[T](pages=0, total=0, data=[])

        return Pagination[T](
            pages=ceil(docs.total // per_page), total=docs.total, data=docs.data
        )

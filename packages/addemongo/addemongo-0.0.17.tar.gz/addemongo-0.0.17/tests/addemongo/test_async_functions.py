from os import environ

import pytest
from dotenv import load_dotenv
from pydantic import BaseModel
from pymongo.results import (
    DeleteResult,
    InsertManyResult,
    InsertOneResult,
    UpdateResult,
)

from addemongo.builders.query import QueryBuilder
from addemongo.connection import AddeMongoConnection

load_dotenv()


class TestModel(BaseModel):
    test: str = "test_mock"


class AddeMongoAsyncFunctionsSuite:
    connection = AddeMongoConnection(environ["mongo_uri"])
    client = connection.async_client("test", "test", TestModel)

    @pytest.mark.asyncio
    async def test_insert_one(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.insert_one(TestModel())
        assert isinstance(result, InsertOneResult) and result.acknowledged

    @pytest.mark.asyncio
    async def test_insert_many(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.insert_many(
            [TestModel(test="test_insert_many_1"), TestModel(test="test_insert_many_2")]
        )
        assert isinstance(result, InsertManyResult)
        assert result.acknowledged
        assert len(result.inserted_ids) == 2

    @pytest.mark.asyncio
    async def test_update_one(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.update_one(
            query=QueryBuilder().set_regex("test", "test"),
            document=TestModel(test="test_update_one"),
        )
        assert isinstance(result, UpdateResult)
        assert result.acknowledged
        assert result.modified_count == 1

    @pytest.mark.asyncio
    async def test_update_many(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.update_many(
            document=TestModel(test="test_update_many"),
            query=QueryBuilder().set_regex("test", "test"),
        )
        assert isinstance(result, UpdateResult)
        assert result.acknowledged
        assert result.modified_count > 1

    @pytest.mark.asyncio
    async def test_find_one(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.find_one(QueryBuilder().set_regex("test", "test"))
        assert isinstance(result, TestModel) and "test" in result.test

    @pytest.mark.asyncio
    async def test_find_many(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.find_many(QueryBuilder().set_regex("test", "test"))
        assert all(["test" in document.test for document in result])

    @pytest.mark.asyncio
    async def test_delete_one(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.delete_one(QueryBuilder().set_regex("test", "test"))
        assert isinstance(result, DeleteResult)
        assert result.deleted_count == 1

    @pytest.mark.asyncio
    async def test_delete_many(self) -> None:
        connection = AddeMongoConnection(environ["mongo_uri"])
        client = connection.async_client("test", "test", TestModel)
        result = await client.delete_many(QueryBuilder().set_regex("test", "test"))
        assert isinstance(result, DeleteResult)
        assert result.deleted_count > 1

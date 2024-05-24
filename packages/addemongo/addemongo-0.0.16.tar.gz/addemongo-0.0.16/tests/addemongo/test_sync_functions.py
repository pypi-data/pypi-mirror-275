from os import environ

from dotenv import load_dotenv
from pydantic import BaseModel
from pymongo.results import (
    InsertManyResult,
    InsertOneResult,
    UpdateResult,
    DeleteResult,
)

from addemongo.builders.query import QueryBuilder
from addemongo.connection import AddeMongoConnection

load_dotenv()


class TestModel(BaseModel):
    test: str = "test_mock"


class AddeMongoSyncFunctionsSuite:
    connection = AddeMongoConnection(environ["mongo_uri"])
    client = connection.sync_client("test", "test", TestModel)

    def test_insert_one(self) -> None:
        result = self.client.insert_one(TestModel())
        assert isinstance(result, InsertOneResult) and result.acknowledged

    def test_insert_many(self) -> None:
        result = self.client.insert_many(
            [TestModel(test="test_insert_many_1"), TestModel(test="test_insert_many_2")]
        )
        assert isinstance(result, InsertManyResult)
        assert result.acknowledged
        assert len(result.inserted_ids) == 2

    def test_update_one(self) -> None:
        result = self.client.update_one(
            query=QueryBuilder().set_regex("test", "test"),
            document=TestModel(test="test_update_one"),
        )
        assert isinstance(result, UpdateResult)
        assert result.acknowledged
        assert result.modified_count == 1

    def test_update_many(self) -> None:
        result = self.client.update_many(
            document=TestModel(test="test_update_many"),
            query=QueryBuilder().set_regex("test", "test"),
        )
        assert isinstance(result, UpdateResult)
        assert result.acknowledged
        assert result.modified_count > 1

    def test_find_one(self) -> None:
        result = self.client.find_one(QueryBuilder().set_regex("test", "test"))
        assert isinstance(result, TestModel) and "test" in result.test

    def test_find_many(self) -> None:
        result = self.client.find_many(QueryBuilder().set_regex("test", "test"))
        assert all(["test" in document.test for document in result])

    def test_delete_one(self) -> None:
        result = self.client.delete_one(QueryBuilder().set_regex("test", "test"))
        assert isinstance(result, DeleteResult)
        assert result.deleted_count == 1

    def test_delete_many(self) -> None:
        result = self.client.delete_many(QueryBuilder().set_regex("test", "test"))
        assert isinstance(result, DeleteResult)
        assert result.deleted_count > 1

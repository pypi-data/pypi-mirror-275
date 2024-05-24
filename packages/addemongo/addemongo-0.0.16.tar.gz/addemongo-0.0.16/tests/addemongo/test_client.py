import pytest
from pydantic import BaseModel

from addemongo._pymongo._client import AddeMongoSyncClient
from addemongo._motor._client import AddeMongoAsyncClient
from addemongo.connection import AddeMongoConnection


class TestModel(BaseModel):
    test: str = "test_mock"


class AddeMongoClientSuite:
    def test_adde_mongo_sync_client(self) -> None:
        connection = AddeMongoConnection()
        client = connection.sync_client("test", "test", TestModel)

        assert isinstance(client, AddeMongoSyncClient)
        assert client.database.name == "test"
        assert client.collection.name == "test"

    @pytest.mark.asyncio
    async def test_adde_mongo_async_client(self) -> None:
        connection = AddeMongoConnection()
        client = connection.async_client("test", "test", TestModel)
        assert isinstance(client, AddeMongoAsyncClient)
        assert client.database.name == "test"
        assert client.collection.name == "test"

from functools import cached_property
from typing import List


def mongo_storage_from_uri(uri: str) -> "Storage":
    return Storage(uri)


class Storage(object):

    def __init__(
        self,
        uri: str,
        database_name: str = "postfinance",
        collection_name: str = "calls",
    ) -> None:
        try:
            from pymongo import MongoClient
            from pymongo.server_api import ServerApi
        except ImportError as e:
            raise ImportError(
                "The Storage class requires the MongoDB Python Driver to be installed."
                "pip install pymongo[srv]"
            ) from e

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi("1"))

        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command("ping")
            print(
                "Pinged your deployment. You successfully connected to MongoDB!"
            )
        except Exception as e:
            raise e

        self.collection = self.client[database_name][collection_name]

    @cached_property
    def calls(self) -> List[dict]:
        return list(self.collection.find())

    @cached_property
    def call_ids(self) -> List[str]:
        return sorted([c["id"] for c in self.calls])

    def get_call_by_id(self, call_id: str) -> dict | None:
        return self.collection.find_one({"id": call_id})

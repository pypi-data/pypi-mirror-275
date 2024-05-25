from pymongo import MongoClient
from pymongo.errors import InvalidURI
from typing import Optional
from os import getenv

mongoUrl: str = getenv("MONGO")


class MongoDB(MongoClient):
    def __init__(self, mongoUri, mongoName: Optional[str]):
        if mongoUri != "":
            self.url = mongoUri
        else:
            self.url = mongoUrl
        self.name = mongoName if mongoName is not None else "FileSharingBot"
        super().__init__(
            self.url
        )
        self.mDb = self[self.name]

    @property
    def mongo(self):
        return self.mDb

    def collection(self, name: str):
        return self.mDb[name]

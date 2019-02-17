import json
from abc import ABC
from concurrent.futures import Future

from backend.grocery_api import GroceryAPI
from requests_futures.sessions import Session

class WegmansAPI(GroceryAPI):
    def get_sku(self, sku: int) -> Future:
        pass

    def get_search(self, query: str) -> Future:
        pass

    def __init__(self):
        self.sess = Session()
        with open("backend/config.json") as f:
            config = json.load(f)

        self.key = config["WEGMANS_KEY"]


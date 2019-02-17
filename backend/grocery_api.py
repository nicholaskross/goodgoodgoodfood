import abc
from concurrent.futures import Future
from requests_futures import sessions

from backend.product import Product


class GroceryAPI(abc.ABC):
    @abc.abstractmethod
    def get_sku(self, sku: int) -> Future:
        raise NotImplemented

    @abc.abstractmethod
    def get_search(self, query: str, cache=None) -> Future:
        raise NotImplemented

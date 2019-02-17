from typing import Dict, List

from backend.grocery_api import GroceryAPI
from backend.product import Product


class ProductCatalog:

    def ensure_search(self, query: str):
        if query not in self.search_queries:
            products = self.api.get_search(query, self.skus).result()
            self.search_queries[query] = [product.sku for product in products]
            for product in products:
                if product.sku not in self.skus:
                    self.skus[product.sku] = product

    def ensure_sku(self, sku: int):
        if sku not in self.skus:
            self.skus[sku] = self.api.get_sku(sku).result()

    def search_query(self, query: str) -> List[Product]:
        query = query.lower().strip()
        self.ensure_search(query)
        return [self.skus[prod] for prod in self.search_queries[query]]

    def get_sku(self, sku: int):
        self.ensure_sku(sku)
        return self.skus[sku]

    def __init__(self, api: GroceryAPI):
        self.search_queries: Dict[str, List[int]] = {}  #: What search queries have been performed so far
        self.skus: Dict[int, Product] = {}
        self.api = api

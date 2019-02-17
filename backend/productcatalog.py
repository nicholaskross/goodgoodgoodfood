from typing import Dict, List
from backend.product import Product


class ProductCatalog:

    def ensure_search(self, query:str):
        pass

    def search_query(self, query:str):
        query = query.lower().strip()
        self.ensure_search(query)

    def __init__(self):
        self.search_queries: Dict[str, List[int]] = {}  #: What search queries have been performed so far
        self.skus: Dict[int, Product]

from typing import Dict, List
from backend.product import Product


class ProductCatalog:
    def __init__(self):
        self.search_queries: Dict[str, List[int]] = {}  #: What search queries have been performed so far
        self.skus: Dict[int, Product]

import json
from abc import ABC
from concurrent.futures import Future, ThreadPoolExecutor
from time import sleep
from typing import Dict, List

from requests import Response

from backend.grocery_api import GroceryAPI
from requests_futures.sessions import FuturesSession

from backend.product import Product
from backend.valueunit import ValueUnit

tpexec = ThreadPoolExecutor(max_workers=32)


class WegmansAPI(GroceryAPI):
    def get_sku(self, sku: int) -> Future:
        """
        Get the SKU of a wegmans product
        :param sku:
        :return: Future of Product
        """
        resp: Future = self.sess.get("https://api.wegmans.io/products/" + str(sku), params=self.default_params)
        resp_prices: Future = self.sess.get(
            "https://api.wegmans.io/products/" + str(sku) + "/prices/" + str(self.store_id),
            params=self.default_params)

        def process_detail():
            try:
                sleep(.01)
                result: Dict = json.loads(resp.result().content)
                result_prices: Dict = json.loads(resp_prices.result().content)

                trade_id = result["tradeIdentifiers"]
                image = None
                if isinstance(trade_id, List) and len(trade_id) > 0:
                    tid0 = trade_id[0]
                    if isinstance(tid0["images"], List) and len(tid0["images"]) > 0:
                        image = tid0["images"][0]

                size = ValueUnit(result["size"]["value"], result["size"]["unitOfMeasure"])

                price = None
                if "price" in result_prices:
                    price = result_prices["price"]

                return Product(sku, image, result["brand"], result["descriptions"]["consumer"], price, size)
            except:
                return None

        return tpexec.submit(process_detail)

    def get_search(self, query: str, cache: Dict[int, Product] = None) -> Future:
        if cache is None:
            cache = dict()

        d = self.default_params.copy()
        d["query"] = query
        resp: Future = self.sess.get("https://api.wegmans.io/products/search", params=d)

        def process_search():
            resp_result: Dict = json.loads(resp.result().content)

            if "results" in resp_result and isinstance(resp_result["results"], List):
                skus = [product["sku"] for product in resp_result["results"]][:50]
            else:
                skus = []

            products_futures = [self.get_sku(sku) if sku not in cache else cache[sku] for sku in skus]
            products = [fut.result() if isinstance(fut, Future) else fut for fut in products_futures]
            products = [product for product in products
                        if product and product.price]  # If we don't have a price, it's not sold at the specific store

            return products

        return tpexec.submit(process_search)

    def __init__(self):
        self.sess = FuturesSession(tpexec)
        with open("config.json") as f:
            config = json.load(f)

        self.store_id = 62

        self.default_params = {
            "Subscription-Key": config["WEGMANS_KEY"],
            "api-version": "2018-10-18"
        }

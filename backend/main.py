# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]

from flask import Blueprint, request, jsonify
import os

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
from backend.func_get_charity import get_charities_from_cart
from backend.productcatalog import ProductCatalog
from backend.wegmans_api import WegmansAPI

app = Blueprint("backend", __name__)

prod_cat = ProductCatalog(WegmansAPI())


@app.route('/search', methods=["GET"])
def search():
    query = request.args.get("query")
    result = prod_cat.search_query(query)
    return jsonify([res.to_dict() for res in result])


@app.route('/similar', methods=["GET"])
def similar():
    sku = int(request.args.get("sku"))
    prod = prod_cat.get_sku(sku)
    similar_products = [compprod for compprod in prod_cat.search_query(prod.description) if
                        (prod.price / 4) < compprod.price < prod.price  # Cheaper but not so cheap that it's wrong
                        and compprod.brand.strip().lower() in ["wegman", "wegman's", "wegmans"]]

    if len(similar_products) == 0:
        return "", 204

    cheapest_price = min((similar_product.price for similar_product in similar_products))
    cheapest_prod = [p for p in similar_products if p.price == cheapest_price][0]

    return jsonify(cheapest_prod.to_dict())


@app.route("/charity", methods=["GET"])
def charity_recommend():
    skus: str = request.args.get("skus")
    sku_arr = [int(sku) for sku in skus.split(",")]

    return jsonify([charity.to_dict() for charity in get_charities_from_cart(sku_arr, prod_cat)])

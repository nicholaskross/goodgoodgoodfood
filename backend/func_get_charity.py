from collections import Counter
from typing import List

import requests

from backend.dictable import Dictable
from backend.product import Product
from backend.productcatalog import ProductCatalog

categories = {
    "haschildren": ["jr", "jr.", "kid", "kids", "cereal"],
    "eco": ["organic"],
    "lotsofseafood": ["fish", "salmon", "tuna", "tilapia", "shrimp", "lobster", "crab", "cod", "fillet"],
    "vegan": ["vegetarian", "vegan", "dairy-free", "soy", "chick'n", "chik'n"]
}


class Charity(Dictable):
    def __init__(self, name, url, description):
        self.name = name
        self.url = url
        self.description = description


def label_categories(food: Product):
    tags = []
    for tag, words in categories.items():
        if any(map(lambda word: word in food.description.lower() or word in food.name.lower(), words)):
            tags.append(tag)

    return tags


def get_charities(category: int = None, search: str = None):
    charityParams = {"app_id": "adcbebfd", "app_key": "68bbeba05b4dd80d57ca19d79965e545", "pageSize": 50,
                     "sort": "RELEVANCE" if search else "RATING"}

    if category:
        charityParams["causeID"] = str(category)

    if search:
        charityParams["search"] = search

    charityData = requests.get("https://api.data.charitynavigator.org/v2/Organizations/", params=charityParams).json()

    return [Charity(c["charityName"], c["websiteURL"], c["tagLine"]) for c in charityData if c["websiteURL"]]


def get_charities_from_cart(shopping_cart: List[int], pc: ProductCatalog):
    causes_table = {
        # Animals
        "Animal Rights, Welfare, and Services": 2,
        "Wildlife Conservation": 1,
        "Zoos and Aquariums": 32,

        # Arts, Culture, Humanities
        "Libraries, Historical Societies and Landmark Preservation": 6,
        "Museums": 3,
        "Performing Arts": 4,
        "Public Broadcasting and Media": 5,

        # Community Development
        "United Ways": 42,
        "Jewish Federations": 43,
        "Community Foundations": 22,
        "Housing and Neighborhood Development": 27,

        # Education
        "Early Childhood Programs and Services": 36,
        "Youth Education Programs and Services": 40,
        "Adult Education Programs and Services": 39,
        "Special Education": 38,
        "Education Policy and Reform": 41,
        "Scholarship and Financial Support": 37,

        # Environment
        "Environmental Protection and Conservation": 11,
        "Botanical Gardens, Parks, and Nature Centers": 10,

        # Health
        "Diseases, Disorders, and Disciplines": 13,
        "Patient and Family Support": 34,
        "Treatment and Prevention Services": 12,
        "Medical Research": 14,

        # Human and Civil Rights
        "Advocacy and Education": 21,

        # Human Services
        "Children's and Family Services": 17,
        "Youth Development, Shelter, and Crisis Services": 16,
        "Food Banks, Food Pantries, and Food Distribution": 18,
        "Multipurpose Human Service Organizations": 15,
        "Homeless Services": 28,
        "Social Services": 29,

        # International
        "Development and Relief Services": 20,
        "International Peace, Security, and Affairs": 19,
        "Humanitarian Relief Supplies": 30,

        # Research and Public Policy
        "Non-Medical Science & Technology Research": 35,
        "Social and Public Policy Research": 24,

        # Religion
        "Religious Activities": 26,
        "Religious Media and Broadcasting": 25}

    # ethnicfoodcount = 0
    # for food in shoppingCart:
    # if food.countryOfOrigin != null:
    # ethnicfoodcount+=1
    # if ethnicfoodcount>=2:
    # weighting_tags.append("ethnicfoods")

    correlates_table = {
        "vegan": "Animal Rights, Welfare, and Services",
        "eco": "Environmental Protection and Conservation",
        "haschildren": "Children's and Family Services",
        "hasmedicalcondition": "Medical Research",
        "ethnicfoods": "Humanitarian Relief Supplies",
        "buyinginbulk": "Food Banks, Food Pantries, and Food Distribution",
        "lotsofseafood": "Zoos and Aquariums",
    }

    causes = Counter()

    for product in shopping_cart:
        for tag in label_categories(pc.get_sku(product)):
            causes[correlates_table[tag]] += 1

    if len(causes) > 0:
        maxcause = causes_table[causes.most_common(1)[0][0]]
    else:
        maxcause = None

    return get_charities(maxcause)

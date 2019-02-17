from backend.dictable import Dictable
from backend.valueunit import ValueUnit


class Product(Dictable):

    def __init__(self, sku: int, image_url: str, brand: str, description: str, price: float, size: ValueUnit,
                 name: str):
        self.name = name
        self.size = size
        self.price = price
        self.description = description
        self.brand = brand
        self.image_url = image_url
        self.sku = sku
        self.unit_price = ValueUnit(self.price / self.size.value, self.size.unit) \
            if price and self.size.value != 0 else None

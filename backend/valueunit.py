from backend.dictable import Dictable


class ValueUnit(Dictable):
    def to_dict(self):
        return self.__dict__.copy()

    def __init__(self, value: float, unit: str):
        self.value = value
        self.unit = unit


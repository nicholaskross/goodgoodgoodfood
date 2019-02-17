import abc
from abc import abstractmethod


class Dictable(abc.ABC):

    def include_in_dict(self, prop:str):
        return True

    def to_dict(self):
        d = dict()
        for prop, value in self.__dict__.items():
            if self.include_in_dict(prop):
                if isinstance(value, Dictable):
                    d[prop] = value.to_dict()
                else:
                    d[prop] = value

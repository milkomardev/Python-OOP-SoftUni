from abc import ABC, abstractmethod
from math import log


class Computer(ABC):

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0

    @property
    @abstractmethod
    def type(self):
        ...

    @property
    @abstractmethod
    def av_processors(self):
        ...

    @property
    @abstractmethod
    def av_ram(self):
        ...

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.av_processors:
            raise ValueError(f"{processor} is not compatible with {self.type} {self.manufacturer} {self.model}!")

        if ram not in self.av_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with {self.type} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += self.av_processors[processor]
        self.price += log(ram, 2) * 100
        return f"Created {self.__repr__()} for {int(self.price)}$."

    def __repr__(self):
        return f"{self.__manufacturer} {self.__model} with {self.processor} and {self.ram}GB RAM"
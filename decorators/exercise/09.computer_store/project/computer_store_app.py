from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    VALID_TYPES = {"Laptop": Laptop, "Desktop Computer": DesktopComputer}

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        try:
            c = self.VALID_TYPES[type_computer](manufacturer, model)

        except KeyError:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        self.warehouse.append(c)
        return c.configure_computer(processor, ram)

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        try:
            computer = [c for c in self.warehouse if c.price <= client_budget and c.processor == wanted_processor and c.ram >= wanted_ram][0]
        except IndexError:
            raise Exception("Sorry, we don't have a computer for you.")
        self.profits += client_budget - computer.price
        self.warehouse.remove(computer)

        return f"{computer} sold for {client_budget}$."

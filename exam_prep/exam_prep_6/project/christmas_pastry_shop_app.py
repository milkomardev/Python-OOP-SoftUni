from typing import List

from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTH_TYPES = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: List[OpenBooth, PrivateBooth] = []
        self.delicacies: List[Stolen, Gingerbread] = []
        self.income: float = 0.00

    def get_delicacy_by_name(self, name):
        existing_delicacy = [d for d in self.delicacies if d.name == name]
        if existing_delicacy:
            return existing_delicacy[0]
        return None

    def get_booth_by_number(self, number):
        existing_booth = [b for b in self.booths if b.booth_number == number]
        if existing_booth:
            return existing_booth[0]
        return None

    def get_free_booth_by_capacity_and_people(self, number_of_people):
        free_booth = [b for b in self.booths if b.capacity >= number_of_people and not b.is_reserved]
        if free_booth:
            return free_booth[0]
        return None

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self.get_delicacy_by_name(name)
        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACY_TYPES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        delicacy = self.VALID_DELICACY_TYPES[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self.get_booth_by_number(booth_number)
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTH_TYPES:
            raise Exception(f"{type_booth} is not a valid booth!")

        booth = self.VALID_BOOTH_TYPES[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        free_booth = self.get_free_booth_by_capacity_and_people(number_of_people)
        if not free_booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        free_booth.reserve(number_of_people)

        return f"Booth {free_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.get_booth_by_number(booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self.get_delicacy_by_name(delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.get_booth_by_number(booth_number)
        bill = booth.price_for_reservation + sum([d.price for d in booth.delicacy_orders])  #TODO: might be wrong
        self.income += bill
        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

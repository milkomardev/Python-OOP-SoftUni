from typing import List

from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    receipt_id = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def get_client_by_phone_number(self, phone_number):
        existing_client = [c for c in self.clients_list if c.phone_number == phone_number]
        if existing_client:
            return existing_client[0]
        return None

    def register_client(self, client_phone_number: str):
        client = self.get_client_by_phone_number(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")

        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if isinstance(meal, Meal):
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return '\n'.join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self.get_client_by_phone_number(client_phone_number)
        if not client:
            self.register_client(client_phone_number)
            client = self.get_client_by_phone_number(client_phone_number)

        for meal, quantity in meal_names_and_quantities.items():
            existing_meal = [m for m in self.menu if m.name == meal]
            if not existing_meal:
                raise Exception(f"{meal} is not on the menu!")

            if existing_meal[0].quantity < quantity:
                raise Exception(
                    f"Not enough quantity of {existing_meal[0].__class__.__name__}: {meal}!")

            meal_in_shopping_cart = [m for m in client.shopping_cart if m.name == meal]
            if meal_in_shopping_cart:
                meal_in_shopping_cart[0].quantity += quantity
            else:
                meal_for_cmr = existing_meal[0].__class__(meal, existing_meal[0].price, quantity)
                client.shopping_cart.append(meal_for_cmr)

            client.bill += quantity * existing_meal[0].price
            existing_meal[0].quantity -= quantity

        return f"Client {client_phone_number} " \
               f"successfully ordered {', '.join([m.name for m in client.shopping_cart])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self.get_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for m in client.shopping_cart:
            meal_in_menu = [mim for mim in self.menu if mim.name == m.name][0]
            meal_in_menu.quantity += m.quantity

        client.bill = 0
        client.shopping_cart.clear()

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self.get_client_by_phone_number(client_phone_number)
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")
        bill_paid = client.bill
        client.bill = 0
        client.shopping_cart.clear()

        FoodOrdersApp.receipt_id += 1

        return f"Receipt #{FoodOrdersApp.receipt_id} with total amount of {bill_paid:.2f} was successfully " \
               f"paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

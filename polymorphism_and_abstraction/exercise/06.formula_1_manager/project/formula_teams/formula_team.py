from abc import ABC, abstractmethod


class FormulaTeam(ABC):

    def __init__(self, budget: int):
        self.budget = budget

    @property
    @abstractmethod
    def sponsors(self):
        ...

    @property
    @abstractmethod
    def expenses(self):
        ...

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        earned_money = 0

        for prize_pool in self.sponsors().values():
            for place in prize_pool:
                if race_pos <= place:
                    earned_money += prize_pool[place]
                    break

        earned_money -= self.expenses()
        self.__budget += earned_money

        return f"The revenue after the race is {earned_money}$. Current budget {self.__budget}$"
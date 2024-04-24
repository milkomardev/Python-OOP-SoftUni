from project.animals.animal import Bird
from project.food import Meat, Fruit, Seed, Vegetable


class Owl(Bird):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Seed, Vegetable]

    @property
    def weight_gained(self):
        return 0.35

    def make_sound(self):
        return "Cluck"


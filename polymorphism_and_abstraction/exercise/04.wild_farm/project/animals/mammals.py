from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def weight_gained(self):
        return 0.10

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]

    @property
    def weight_gained(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_gained(self):
        return 1.00

    def make_sound(self):
        return "ROAR!!!"
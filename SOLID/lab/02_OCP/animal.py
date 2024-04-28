from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species

    @staticmethod
    @abstractmethod
    def make_sound():
        ...


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


class Dog(Animal):
    @staticmethod
    def make_sound():
        return "woof-woof"


class Cat(Animal):
    @staticmethod
    def make_sound():
        return 'meow'


class Cow(Animal):
    @staticmethod
    def make_sound():
        return 'moo'


animals = [Cat('cat'), Dog('dog'), Cow('cow')]
animal_sound(animals)

print(animals[0].__class__.__name__)
print(animals[0].species)
## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]

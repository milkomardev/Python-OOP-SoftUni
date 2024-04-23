from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    AC_ON = 0.9

    def drive(self, distance):
        total_consumption = self.fuel_consumption + Car.AC_ON
        if self.fuel_quantity >= total_consumption * distance:
            self.fuel_quantity -= total_consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_ON = 1.6
    TANK_CAPACITY = 0.95

    def drive(self, distance):
        total_consumption = self.fuel_consumption + Truck.AC_ON
        if self.fuel_quantity >= total_consumption * distance:
            self.fuel_quantity -= total_consumption * distance

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.TANK_CAPACITY


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
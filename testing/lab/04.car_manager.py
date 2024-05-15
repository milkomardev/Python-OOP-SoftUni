from unittest import TestCase, main


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class TestCar(TestCase):
    def setUp(self) -> None:
        self.car = Car("BMW", "M6", 20, 80)

    def test_init_method_correct(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("M6", self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(80, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_init_with_empty_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "M6", 20, 80)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_init_with_empty_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("BMW", "", 20, 80)

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_init_with_zero_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("BMW", "M6", 0, 80)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_init_with_negative_fuel_consumption_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("BMW", "M6", -5, 80)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_init_with_zero_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("BMW", "M6", 20, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_init_with_negative_fuel_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("BMW", "M6", 20, -80)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_init_with_negative_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("BMW", "M6", 20, 80)
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_with_zero_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_with_negative_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_increases_fuel_amount(self):
        self.car.refuel(20)
        self.assertEqual(20, self.car.fuel_amount)

    def test_refuel_with_amount_bigger_than_capacity_sets_amount_equal_to_capacity(self):
        self.car.refuel(100)
        self.assertEqual(80, self.car.fuel_amount)

    def test_drive_needed_fuel_more_than_current_fuel_amount_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_needed_fuel_is_enough_and_fuel_amount_is_reduced(self):
        self.car.refuel(80)
        self.car.drive(100)
        self.assertEqual(60, self.car.fuel_amount)


if __name__ == '__main__':
    main()
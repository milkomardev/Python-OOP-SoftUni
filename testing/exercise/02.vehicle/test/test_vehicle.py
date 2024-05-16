from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 200.5)

    def test_vehicle_class_correct_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(200.5, self.vehicle.horse_power)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_vehicle_fuel_not_enough_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_method_with_enough_fuel_decreases_fuel(self):
        self.vehicle.drive(10)
        self.assertEqual(8, self.vehicle.fuel)

    def test_refuel_with_more_amount_than_capacity_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(25)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_valid_amount_increases_current_fuel(self):
        self.vehicle.fuel = 2
        self.vehicle.refuel(15)
        self.assertEqual(17, self.vehicle.fuel)

    def test__str__method_returns_str(self):
        self.assertEqual(f"The vehicle has 200.5 " 
                         f"horse power with 20.5 fuel left and "
                         f"1.25 fuel consumption", self.vehicle.__str__())


if __name__ == '__main__':
    main()
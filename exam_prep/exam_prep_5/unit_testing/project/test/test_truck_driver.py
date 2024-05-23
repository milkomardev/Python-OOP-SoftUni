from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.truck_driver = TruckDriver("Gosho", 10)

    def test_constructor(self):
        self.assertEqual("Gosho", self.truck_driver.name)
        self.assertEqual(10, self.truck_driver.money_per_mile)
        self.assertEqual({}, self.truck_driver.available_cargos)
        self.assertEqual(0, self.truck_driver.earned_money)
        self.assertEqual(0, self.truck_driver.miles)

    def test_invalid_earned_money_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.truck_driver.earned_money = -1
        self.assertEqual("Gosho went bankrupt.", str(ve.exception))

    def test_add_cargo_offer_method_updates_available_cargos_list(self):
        result = self.truck_driver.add_cargo_offer("Sofia", 200)
        self.assertEqual("Cargo for 200 to Sofia was added as an offer.", result)
        self.assertEqual({"Sofia": 200}, self.truck_driver.available_cargos)

    def test_add_cargo_offer_method_add_same_cargo_raises(self):
        self.truck_driver.add_cargo_offer("Sofia", 200)
        with self.assertRaises(Exception) as ex:
            self.truck_driver.add_cargo_offer("Sofia", 200)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer_no_offers_raises(self):
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer_updates_earned_money_and_miles_returns_valid_data(self):
        self.truck_driver.add_cargo_offer("Sofia", 100)
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Gosho is driving 100 to Sofia.", result)
        self.assertEqual(1000, self.truck_driver.earned_money)
        self.assertEqual(100, self.truck_driver.miles)

    def test_drive_best_cargo_offer_multiple_offers_updates_earned_money_and_miles_returns_valid_data(self):
        self.truck_driver.add_cargo_offer("Sofia", 100)
        self.truck_driver.add_cargo_offer("Plovdiv", 500)
        result = self.truck_driver.drive_best_cargo_offer()
        self.assertEqual("Gosho is driving 500 to Plovdiv.", result)
        self.assertEqual(4960, self.truck_driver.earned_money)
        self.assertEqual(500, self.truck_driver.miles)

    def test_eat_method_updates_money_earned(self):
        self.truck_driver.add_cargo_offer("Sofia", 300)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(2980, self.truck_driver.earned_money)

    def test_sleep_method_updates_money_earned(self):
        self.truck_driver.add_cargo_offer("Sofia", 1000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(9875, self.truck_driver.earned_money)

    def test_pump_gas_method_updates_money_earned(self):
        self.truck_driver.add_cargo_offer("Sofia", 1500)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(14_335, self.truck_driver.earned_money)

    def test_repair_truck_method_updates_money_earned(self):
        self.truck_driver.add_cargo_offer("Sofia", 10_000)
        self.truck_driver.drive_best_cargo_offer()
        self.assertEqual(88_250, self.truck_driver.earned_money)

    def test__repr__method_returns_correct_message(self):
        result = self.truck_driver.__repr__()
        self.assertEqual("Gosho has 0 miles behind his back.", result)

if __name__ == "__main__":
    main()
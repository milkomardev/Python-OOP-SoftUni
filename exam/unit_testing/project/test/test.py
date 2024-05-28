from unittest import TestCase, main

from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("car", "sport", 1000, 1000)

    def test_constructor(self):
        self.assertEqual("car", self.car.model)
        self.assertEqual("sport", self.car.car_type)
        self.assertEqual(1000, self.car.mileage)
        self.assertEqual(1000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_1_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("car", "sport", 1000, 1)
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_price_less_than_1_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("car", "sport", 1000, -1)
        self.assertEqual("Price should be greater than 1.0!", str(ve.exception))

    def test_mileage_100_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("car", "sport", 100, 1000)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_mileage_less_than_100_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car = SecondHandCar("car", "sport", 10, 1000)
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ve.exception))

    def test_set_promotional_price_method_new_price_higher_than_current_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(2000)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_method_new_price_same_as_current_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(1000)
        self.assertEqual("You are supposed to decrease the price!", str(ve.exception))

    def test_set_promotional_price_updates_price_and_returns_correct_info(self):
        result = self.car.set_promotional_price(900)
        self.assertEqual("The promotional price has been successfully set.", result)
        self.assertEqual(900, self.car.price)

    def test_need_repair_method_repair_price_higher_than_half_car_price_returns_correct_message(self):
        result = self.car.need_repair(600, "transmission")
        self.assertEqual("Repair is impossible!", result)
        self.assertEqual(1000, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_need_repair_method_updates_repairs_list_and_price_and_returns_correct_message(self):
        result = self.car.need_repair(400, "breaks")
        self.assertEqual('Price has been increased due to repair charges.', result)
        self.assertEqual(1400, self.car.price)
        self.assertEqual(["breaks"], self.car.repairs)

    def test__gt__method_returns_message_if_car_types_are_different(self):
        self.other_car = SecondHandCar("other", "other", 1000, 1000)
        result = self.car.__gt__(self.other_car)
        self.assertEqual("Cars cannot be compared. Type mismatch!", result)

    def test__gt__method_returns_True_if_car_price_higher_than_other_car_price(self):
        self.other_car = SecondHandCar("other", "sport", 1000, 900)
        result = self.car.__gt__(self.other_car)
        self.assertEqual(True, result)

    def test__gt__method_returns_False_if_car_price_lower_than_other_car_price(self):
        self.other_car = SecondHandCar("other", "sport", 1000, 1000)
        result = self.car.__gt__(self.other_car)
        self.assertEqual(False, result)

    def test__gt__method_returns_False_if_car_price_same_as_other_car_price(self):
        self.other_car = SecondHandCar("other", "sport", 1000, 9000)
        result = self.car.__gt__(self.other_car)
        self.assertEqual(False, result)

    def test__str__method_returns_correct_info(self):
        result = self.car.__str__()
        self.assertEqual("Model car | Type sport | Milage 1000km\n"
                         "Current price: 1000.00 | Number of Repairs: 0", result)


if __name__ == "__main__":
    main()

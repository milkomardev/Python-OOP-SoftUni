from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(10)

    def test_plantation_class_correct_initialization(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_negative_size_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Plantation(-2)
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_method_updates_workers_list(self):
        result = self.plantation.hire_worker("Pesho")
        self.assertEqual(["Pesho"], self.plantation.workers)
        self.assertEqual("Pesho successfully hired.", result)

    def test_hire_worker_method_raises_value_error_when_hiring_the_same_worker(self):
        self.plantation.hire_worker("Pesho")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Pesho")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test__len__method_returns_total_count_of_planted_plants_one_worker(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho","Tulip")
        self.plantation.planting("Pesho","Rose")
        self.assertEqual(2, self.plantation.__len__())

    def test__len__method_returns_total_count_of_planted_plants_many_workers(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Gosho")
        self.plantation.planting("Pesho","Tulip")
        self.plantation.planting("Pesho","Rose")
        self.plantation.planting("Gosho","Rose")
        self.assertEqual(3, self.plantation.__len__())

    def test__len_method_returns_zero_if_no_planted_plants(self):
        self.assertEqual(0, self.plantation.__len__())

    def test_planting_method_raises_value_error_if_worker_not_hired(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "Tulip")
        self.assertEqual("Worker with name Pesho is not hired!", str(ve.exception))

    def test_planting_method_raises_value_error_if_plantation_is_full(self):
        self.plantation.size = 0
        self.plantation.hire_worker("Pesho")
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "Tulip")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_method_creates_new_key_value_pair_in_plants_dict_with_list_for_value_for_first_planted_plant_for_worker(self):
        self.plantation.hire_worker("Pesho")
        result = self.plantation.planting("Pesho", "Rose")
        self.assertEqual({"Pesho": ["Rose"]}, self.plantation.plants)
        self.assertEqual("Pesho planted it's first Rose.", result)

    def test_planting_method_appends_new_planted_plant_to_existing_key_value_pair(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "Rose")
        result = self.plantation.planting("Pesho", "Tulip")
        self.assertEqual({"Pesho": ["Rose", "Tulip"]}, self.plantation.plants)
        self.assertEqual("Pesho planted Tulip.", result)

    def test__str__method_returns_correct_information_with_many_workers_and_plants(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Gosho")
        self.plantation.planting("Pesho", "Rose")
        self.plantation.planting("Gosho", "Tulip")
        result = self.plantation.__str__()
        self.assertEqual("Plantation size: 10\n"
                         "Pesho, Gosho\n"
                         "Pesho planted: Rose\n"
                         "Gosho planted: Tulip", result)

    def test__str__method_returns_correct_information_with_many_workers_and_multiple_plants(self):
            self.plantation.hire_worker("Pesho")
            self.plantation.hire_worker("Gosho")
            self.plantation.planting("Pesho", "Rose")
            self.plantation.planting("Pesho", "Rose")
            self.plantation.planting("Gosho", "Tulip")
            self.plantation.planting("Gosho", "Tulip")
            result = self.plantation.__str__()
            self.assertEqual("Plantation size: 10\n"
                             "Pesho, Gosho\n"
                             "Pesho planted: Rose, Rose\n"
                             "Gosho planted: Tulip, Tulip", result)

    def test__str__method_returns_correct_information_with_one_worker_and_one_plant(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "Rose")
        result = self.plantation.__str__()
        self.assertEqual("Plantation size: 10\n"
                         "Pesho\n"
                         "Pesho planted: Rose", result)

    def test__str__method_returns_correct_information_with_one_worker_and_plants(self):
            self.plantation.hire_worker("Pesho")
            self.plantation.planting("Pesho", "Rose")
            self.plantation.planting("Pesho", "Tulip")
            result = self.plantation.__str__()
            self.assertEqual("Plantation size: 10\n"
                             "Pesho\n"
                             "Pesho planted: Rose, Tulip", result)

    def test__str__method_returns_correct_information_without_workers_and_plants(self):
        result = self.plantation.__str__()
        self.assertEqual("Plantation size: 10\n", result)

    def test__str__method_returns_correct_information_with_workers_and_without_plants(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Gosho")
        result = self.plantation.__str__()
        self.assertEqual("Plantation size: 10\n"
                         "Pesho, Gosho", result)

    def test__repr__method_returns_correct_data_with_workers(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.hire_worker("Gosho")
        result = self.plantation.__repr__()
        self.assertEqual("Size: 10\n"
                         "Workers: Pesho, Gosho", result)

    def test__repr__method_returns_correct_data_with_one_worker(self):
        self.plantation.hire_worker("Pesho")
        result = self.plantation.__repr__()
        self.assertEqual("Size: 10\n"
                         "Workers: Pesho", result)

    def test__repr__method_returns_correct_data_without_workers(self):
        result = self.plantation.__repr__()
        self.assertEqual("Size: 10\n"
                         "Workers: ", result)

if __name__ == '__main__':
    main()
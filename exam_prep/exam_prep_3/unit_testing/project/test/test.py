from unittest import TestCase, main

from project.robot import Robot


class TestRobot(TestCase):
    def setUp(self) -> None:
        self.military_robot = Robot('1', 'Military', 10, 10)
        self.education_robot = Robot('2', 'Education', 10, 10)
        self.entertainment_robot = Robot('3', 'Entertainment', 10, 10)
        self.humanoids_robot = Robot('4', 'Humanoids', 10, 10)

    def test_constructor(self):
        self.assertEqual('1', self.military_robot.robot_id)
        self.assertEqual('Military', self.military_robot.category)
        self.assertEqual(10, self.military_robot.available_capacity)
        self.assertEqual(10, self.military_robot.price)
        self.assertEqual([], self.military_robot.hardware_upgrades)
        self.assertEqual([], self.military_robot.software_updates)
        self.assertEqual('Education', self.education_robot.category)
        self.assertEqual('Entertainment', self.entertainment_robot.category)
        self.assertEqual('Humanoids', self.humanoids_robot.category)
        self.assertEqual(1.5, self.military_robot.PRICE_INCREMENT)
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'],
                         self.military_robot.ALLOWED_CATEGORIES)

    def test_invalid_category_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('1', 'invalid', 10, 10)
        self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'",
                         str(ve.exception))

    def test_invalid_price_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.robot = Robot('1', 'Military', 10, -10)
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_upgrade_method_adds_component_to_hardware_upgrades_list(self):
        result = self.military_robot.upgrade("RAM", 2)
        self.assertEqual(['RAM'], self.military_robot.hardware_upgrades)
        self.assertEqual(13, self.military_robot.price)
        self.assertEqual("Robot 1 was upgraded with RAM.", result)

    def test_upgrade_method_does_not_upgrade_with_the_same_hardware_component(self):
        self.military_robot.upgrade("RAM", 2)
        self.assertEqual(['RAM'], self.military_robot.hardware_upgrades)
        result = self.military_robot.upgrade("RAM", 2)
        self.assertEqual("Robot 1 was not upgraded.", result)
        self.assertEqual(['RAM'], self.military_robot.hardware_upgrades)

    def test_update_method_adds_new_update_to_software_updates_list(self):
        result = self.military_robot.update(1.2, 5)
        self.assertEqual([1.2], self.military_robot.software_updates)
        self.assertEqual(5, self.military_robot.available_capacity)
        self.assertEqual('Robot 1 was updated to version 1.2.', result)

    def test_update_method_adds_higher_version_to_software_updates_list(self):
        self.military_robot.update(2.0, 2)
        self.assertEqual([2.0], self.military_robot.software_updates)
        self.assertEqual(8, self.military_robot.available_capacity)
        result = self.military_robot.update(3.0, 2)
        self.assertEqual([2.0, 3.0], self.military_robot.software_updates)
        self.assertEqual(6, self.military_robot.available_capacity)
        self.assertEqual('Robot 1 was updated to version 3.0.', result)

    def test_update_method_available_capacity_less_than_needed_doesnt_update_software_updates_list(self):
        self.military_robot.available_capacity = 4
        result = self.military_robot.update(1.2, 5)
        self.assertEqual([], self.military_robot.software_updates)
        self.assertEqual(4, self.military_robot.available_capacity)
        self.assertEqual("Robot 1 was not updated.", result)

    def test_update_method_version_lower_than_highest_update_doesnt_update_software_updates_list(self):
        self.military_robot.update(2.0, 2)
        self.assertEqual([2.0], self.military_robot.software_updates)
        self.assertEqual(8, self.military_robot.available_capacity)
        result = self.military_robot.update(1.5, 2)
        self.assertEqual("Robot 1 was not updated.", result)
        self.assertEqual([2.0], self.military_robot.software_updates)
        self.assertEqual(8, self.military_robot.available_capacity)

    def test__gt__method_first_robot_more_expensive_than_second_robot(self):
        self.military_robot.price = 100
        result = self.military_robot.__gt__(self.education_robot)
        self.assertEqual('Robot with ID 1 is more expensive than Robot with ID 2.', result)

    def test__gt__method_first_robot_same_price_as_second_robot(self):
        result = self.military_robot.__gt__(self.education_robot)
        self.assertEqual('Robot with ID 1 costs equal to Robot with ID 2.', result)

    def test__gt__method_first_robot_cheaper_than_second_robot(self):
        self.education_robot.price = 100
        result = self.military_robot.__gt__(self.education_robot)
        self.assertEqual('Robot with ID 1 is cheaper than Robot with ID 2.', result)


if __name__ == '__main__':
    main()

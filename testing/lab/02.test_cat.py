from unittest import TestCase, main


class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class TestCat(TestCase):
    def setUp(self) -> None:
        self.cat = Cat("Tom")

    def test_cat_class_correct_initialization(self):
        self.assertEqual("Tom", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_set_fed_and_sleepy_and_increase_size(self):
        self.cat.eat()
        self.assertEqual(True, self.cat.fed)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_eat_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_sleep_when_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_sleep_when_fed_and_sleepy_update_sleepy(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == "__main__":
    main()

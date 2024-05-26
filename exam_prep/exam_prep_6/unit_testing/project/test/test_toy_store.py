from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy_store = ToyStore()

    def test_constructor(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)

    def test_add_toy_method_updates_correct_shelf(self):
        result = self.toy_store.add_toy("A", "Lion")
        self.assertEqual("Lion", self.toy_store.toy_shelf["A"])
        self.assertEqual("Toy:Lion placed successfully!", result)

    def test_add_toy_method_add_to_not_existing_shelf_raises(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("Z", "Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_method_add_same_toy_raises(self):
        self.toy_store.add_toy("A", "Lion")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Lion")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_method_add_to_taken_shelf_raises(self):
        self.toy_store.add_toy("A", "Lion")
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Bear")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_remove_toy_method_removes_toy_from_shelf(self):
        self.toy_store.add_toy("A", "Lion")
        result = self.toy_store.remove_toy("A", "Lion")
        self.assertEqual(None, self.toy_store.toy_shelf["A"])
        self.assertEqual("Remove toy:Lion successfully!", result)

    def test_remove_toy_method_shelf_not_existing_raises(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("Z", "Lion")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_toy_method_toy_to_remove_different_than_toy_on_shelf_raises(self):
        self.toy_store.add_toy("A", "Lion")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Bear")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))


if __name__ == '__main__':
    main()

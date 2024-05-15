from unittest import TestCase, main


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class TestList(TestCase):

    def setUp(self) -> None:
        self.test_list = IntegerList(2, 3, 4)

    def test_list_class_correct_initialization(self):
        self.assertEqual([2, 3, 4], self.test_list.get_data())
        self.assertEqual([2, 3, 4], self.test_list._IntegerList__data)

    def test_init_list_not_integers_are_not_added(self):
        self.test_list = IntegerList(2, 3, 4.5, [], {}, "23", True)
        self.assertEqual([2, 3], self.test_list.get_data())

    def test_get_data_returns_list_with_the_elements(self):
        self.assertEqual([2, 3, 4], self.test_list.get_data())

    def test_add_wrong_type_element_in_list(self):
        self.assertEqual([2, 3, 4], self.test_list.get_data())

        with self.assertRaises(Exception) as ex:
            for el in [[], {}, 3.4, "asd", True]:
                self.test_list.add(el)

            self.assertEqual("Element is not Integer", str(ex.exception))

        self.assertEqual([2, 3, 4], self.test_list.get_data())

    def test_add_integer_in_list(self):
        self.assertEqual([2, 3, 4], self.test_list.get_data())

        self.test_list.add(5)
        self.assertEqual([2, 3, 4, 5], self.test_list.get_data())

    def test_remove_index_index_equal_to_len_or_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.test_list.remove_index(len(self.test_list.get_data()))

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_updating_list(self):
        self.assertEqual([2, 3, 4], self.test_list.get_data())
        self.test_list.remove_index(0)
        self.assertEqual([3, 4], self.test_list.get_data())

    def test_get_method_index_equal_to_len_or_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.test_list.get(len(self.test_list.get_data()))

        self.assertEqual('Index is out of range', str(ex.exception))

    def test_get_method_gets_element_with_valid_index(self):
        result = self.test_list.get(0)
        self.assertEqual(2, result)

    def test_insert_method_index_equal_to_len_or_out_of_range(self):
        with self.assertRaises(Exception) as ex:
            self.test_list.insert(len(self.test_list.get_data()), 9)

        self.assertEqual('Index is out of range', str(ex.exception))

    def test_insert_method_with_element_not_integer(self):
        self.assertEqual(3, len(self.test_list.get_data()))

        with self.assertRaises(Exception) as ex:
            for el in [[], {}, 3.4, "asd", True]:
                self.test_list.insert(0, el)

            self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(3, len(self.test_list.get_data()))

    def test_insert_method_adds_element_to_the_list(self):
        result = self.test_list.insert(0, 9)
        self.assertEqual([9, 2, 3, 4], self.test_list.get_data())

    def test_get_biggest_method_returns_biggest_element(self):
        result = self.test_list.get_biggest()
        self.assertEqual(4, result)

    def test_get_index_method_returns_correct_index(self):
        result = self.test_list.get_index(3)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()

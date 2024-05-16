from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Lion", "Cat", "Roar")

    def test_mammal_class_correct_initialization(self):
        self.assertEqual("Lion", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Roar", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method_returns_sound(self):
        self.assertEqual("Lion makes Roar", self.mammal.make_sound())

    def test_get_kingdom_method_returns_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method_returns_info(self):
        self.assertEqual("Lion is of type Cat", self.mammal.info())


if __name__ == '__main__':
    main()
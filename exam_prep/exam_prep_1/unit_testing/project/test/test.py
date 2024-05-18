from unittest import TestCase, main

from project.movie import Movie


class MovieTest(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("Name", 2000, 8.0)

    def test_movie_class_correct_initiation(self):
        self.assertEqual("Name", self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(8.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_empty_string_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_before_1887_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_method_actor_already_in_list_returns_message(self):
        self.movie.actors = ["Sandra Bullock"]
        result = self.movie.add_actor("Sandra Bullock")
        self.assertEqual("Sandra Bullock is already added in the list of actors!", result)

    def test_add_actor_updates_actors_list(self):
        self.movie.add_actor("Sandra Bullock")
        self.assertEqual(["Sandra Bullock"], self.movie.actors)

    def test__gt__method_returns_first_is_better_than_second(self):
        self.second_movie = Movie("second", 2005, 7.0)
        result = self.movie.__gt__(self.second_movie)
        self.assertEqual('"Name" is better than "second"', result)

    def test__gt__method_returns_second_is_better_than_first(self):
        self.second_movie = Movie("second", 2005, 9.0)
        result = self.movie.__gt__(self.second_movie)
        self.assertEqual('"second" is better than "Name"', result)

    def test__repr__method_returns_correct_string_without_actors(self):
        result = self.movie.__repr__()
        self.assertEqual("Name: Name\n" + "Year of Release: 2000\n" + f"Rating: 8.00\n" + "Cast: ", result)

    def test__repr__method_returns_correct_string_with_actors(self):
        self.movie.add_actor('Sandra Bullock')
        self.movie.add_actor('Scarlett Johansson')
        result = self.movie.__repr__()
        self.assertEqual(
            "Name: Name\n" + "Year of Release: 2000\n" + f"Rating: 8.00\n" + "Cast: Sandra Bullock, Scarlett Johansson",
            result)


if __name__ == '__main__':
    main()

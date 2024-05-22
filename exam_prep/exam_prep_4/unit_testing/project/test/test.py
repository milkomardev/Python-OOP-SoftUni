from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer('test', 20, 100)

    def test_constructor(self):
        self.assertEqual("test", self.player.name)
        self.assertEqual(20, self.player.age)
        self.assertEqual(100, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_invalid_name_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('te', 20, 100)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_invalid_age_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer('Test', 15, 100)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_updates_wins_list(self):
        self.assertEqual([], self.player.wins)
        self.player.add_new_win("Win")
        self.assertEqual(["Win"], self.player.wins)

    def test_add_same_win_returns_message_and_doesnt_update_wins_list(self):
        self.player.add_new_win("Win")
        self.assertEqual(["Win"], self.player.wins)
        result = self.player.add_new_win("Win")
        self.assertEqual(["Win"], self.player.wins)
        self.assertEqual("Win has been already added to the list of wins!", result)

    def test__lt__method_returns_correct_first_player_better_than_second(self):
        self.player2 = TennisPlayer("Test2", 25, 50)
        result = self.player.__lt__(self.player2)
        self.assertEqual("test is a better player than Test2", result)

    def test__lt__method_returns_correct_second_player_better_than_first(self):
        self.player2 = TennisPlayer("Test2", 25, 150)
        result = self.player.__lt__(self.player2)
        self.assertEqual("Test2 is a top seeded player and he/she is better than test", result)

    def test__str__method_returns_correct_data_without_wins(self):
        result = self.player.__str__()
        self.assertEqual(f"Tennis Player: test\n" \
               f"Age: 20\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: ", result)

    def test__str__method_returns_correct_data_with_win(self):
        self.player.add_new_win("Win")
        result = self.player.__str__()
        self.assertEqual(f"Tennis Player: test\n" \
               f"Age: 20\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: Win", result)

    def test__str__method_returns_correct_data_with_wins(self):
        self.player.add_new_win("Win")
        self.player.add_new_win("Win2")
        result = self.player.__str__()
        self.assertEqual(f"Tennis Player: test\n" \
               f"Age: 20\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: Win, Win2", result)

if __name__ == '__main__':
    main()
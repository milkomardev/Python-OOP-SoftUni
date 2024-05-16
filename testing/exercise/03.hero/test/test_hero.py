from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("username", 1, 1000, 100)
        self.enemy = Hero("enemy", 1, 1000, 100)

    def test_hero_class_correct_initialization(self):
        self.assertEqual("username", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(1000, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_if_enemy_is_the_same_as_hero_raise_exception(self):
        self.enemy = Hero("username", 1, 1000, 100)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_with_zero_health_raises_exception(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_hero_with_negative_health_raises_exception(self):
        self.hero.health = -20
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_with_zero_health_raises_exception(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight enemy. He needs to rest", str(ve.exception))

    def test_battle_enemy_with_negative_health_raises_exception(self):
        self.enemy.health = -20
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight enemy. He needs to rest", str(ve.exception))

    def test_battle_if_both_dead(self):
        self.hero.health = 100
        self.enemy.health = 100
        result = self.hero.battle(self.enemy)
        self.assertEqual("Draw", result)

    def test_battle_enemy_dead_and_hero_stats_improve(self):
        self.hero.damage = 2000
        result = self.hero.battle(self.enemy)
        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(905, self.hero.health)
        self.assertEqual(2005, self.hero.damage)

    def test_battle_hero_dead_and_enemy_stats_improve(self):
        self.enemy.damage = 2000
        result = self.hero.battle(self.enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(905, self.enemy.health)
        self.assertEqual(2005, self.enemy.damage)

    def test__str__method_returns_info(self):
        self.assertEqual(f"Hero username: 1 lvl\n"
                         f"Health: 1000\n"
                         f"Damage: 100\n", self.hero.__str__())


if __name__ == '__main__':
    main()
from unittest import TestCase, main


class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'




class WorkerTests(TestCase):

    def setUp(self) -> None:
        self.worker = Worker("Test", 1000, 100)

    def test_worker_class_correct_initialisation(self):
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_not_enough_energy(self):
        self.worker = Worker("Test", 1000, 0)
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_negative_energy(self):
        self.worker = Worker("Test", 1000, -1)
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_work_update_energy_decreased_and_money_increased(self):
        self.assertEqual(0, self.worker.money)
        self.assertEqual(100, self.worker.energy)

        self.worker.work()
        self.assertEqual(1000, self.worker.money)
        self.assertEqual(99, self.worker.energy)

        self.worker.work()
        self.assertEqual(2000, self.worker.money)
        self.assertEqual(98, self.worker.energy)

    def test_rest_increase_energy(self):
        self.assertEqual(100, self.worker.energy)
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_get_info(self):
        self.assertEqual('Test has saved 0 money.', self.worker.get_info())


if __name__ == "__main__":
    main()
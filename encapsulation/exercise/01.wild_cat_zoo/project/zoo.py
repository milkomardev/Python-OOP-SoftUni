from typing import List

from project.animal import Animal
from project.cheetah import Cheetah
from project.lion import Lion
from project.tiger import Tiger
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)

        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, name: str) -> str:
        try:
            worker_to_fire = next(filter(lambda x: x.name == name, self.workers))
        except StopIteration:
            return f"There is no {name} in the zoo"

        self.workers.remove(worker_to_fire)

        return f"{name} fired successfully"

    def pay_workers(self) -> str:
        needed_budget = sum([w.salary for w in self.workers])
        if self.__budget < needed_budget:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= needed_budget

        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self) -> str:
        needed_budget = sum([a.money_for_care for a in self.animals])
        if self.__budget < needed_budget:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= needed_budget

        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        result += "\n".join([f"{l}" for l in lions]) + "\n"

        result += f"----- {len(tigers)} Tigers:\n"
        result += "\n".join([f"{t}" for t in tigers]) + "\n"

        result += f"----- {len(cheetahs)} Cheetahs:\n"
        result += "\n".join([f"{c}" for c in cheetahs])

        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result += f"----- {len(keepers)} Keepers:\n"
        result += "\n".join([f"{k}" for k in keepers]) + "\n"

        result += f"----- {len(caretakers)} Caretakers:\n"
        result += "\n".join([f"{c}" for c in caretakers]) + "\n"

        result += f"----- {len(vets)} Vets:\n"
        result += "\n".join([f"{v}" for v in vets])

        return result

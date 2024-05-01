import copy
from abc import ABC


class Person(ABC):
    def __init__(self, position):
        self.position = position


class FreePerson(Person):

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super().__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


prisoner = Prisoner()
prisoner2 = Prisoner()
print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(prisoner2.position)
prisoner2.position = [5,6]
print(prisoner2.position)
print(prisoner2.PRISON_LOCATION)

print(f"The location of the prison: {Prisoner.PRISON_LOCATION}")
print(f"The current position of the prisoner: {prisoner.position}")


print(Prisoner.PRISON_LOCATION)
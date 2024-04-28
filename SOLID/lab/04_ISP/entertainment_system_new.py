from abc import ABC, abstractmethod


class Cable(ABC):
    @abstractmethod
    def connect(self, end1, end2):
        ...


class HDMICable(Cable):
    def connect(self, end1, end2):
        return f"Connect {end1} to {end2} via HDMI cable"


class RCACable(Cable):
    def connect(self, end1, end2):
        return f"Connect {end1} to {end2} via RCA cable"


class EthernetCable(Cable):
    def connect(self, end1, end2):
        return f"Connect {end1} to {end2} via Ethernet cable"


class PowerCable(Cable):
    def connect(self, end1, end2='power outlet'):
        return f"Connect {end1} to {end2} via power cable"


class Television:
    def __repr__(self):
        return 'TV'


class Router:
    def __repr__(self):
        return 'Router'


class GameConsole:
    def __repr__(self):
        return 'Game Console'


class DVDPlayer:
    def __repr__(self):
        return 'DVD Player'


hdmi = HDMICable()
tv = Television()
game_console = GameConsole()
power_cable = PowerCable()

print(power_cable.connect(game_console))
print(hdmi.connect(tv, game_console))
print(power_cable.connect(tv))
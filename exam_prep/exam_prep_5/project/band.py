from typing import List

from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer


class Band:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Singer, Drummer, Guitarist] = []
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Band name should contain at least one character!")
        self.__name = value

    def __str__(self):
        return f"{self.name} with {len(self.members)} members."


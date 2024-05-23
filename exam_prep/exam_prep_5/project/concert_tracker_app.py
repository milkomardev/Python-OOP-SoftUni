from typing import List
from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {
        "Guitarist": Guitarist,
        "Drummer": Drummer,
        "Singer": Singer
    }

    def __init__(self):
        self.bands: List[Band] = []
        self.musicians: List[Singer, Guitarist, Drummer] = []
        self.concerts: List[Concert] = []

    def get_musician_by_name(self, name):
        existing_musician = [m for m in self.musicians if m.name == name]
        if existing_musician:
            return existing_musician[0]
        return None

    def get_musician_by_name_in_a_band(self, musician_name, band: Band):
        existing_musician = [m for m in band.members if m.name == musician_name]
        if existing_musician:
            return existing_musician[0]
        return None

    def get_band_by_name(self, name):
        existing_band = [b for b in self.bands if b.name == name]
        if existing_band:
            return existing_band[0]
        return None

    def get_concert_by_place(self, place):
        existing_concert = [c for c in self.concerts if c.place == place]
        if existing_concert:
            return existing_concert[0]
        return None

    def members_can_play_at_concert(self, concert, guitarists, singers, drummers, band):
        flag = False
        if concert.genre == "Rock":
            for guitarist in guitarists:
                if "play rock" not in guitarist.skills:
                    flag = True
                    break
            if not flag:
                for singer in singers:
                    if "sing high pitch notes" not in singer.skills:
                        flag = True
                        break
            if not flag:
                for drummer in drummers:
                    if "play the drums with drumsticks" not in drummer.skills:
                        flag = True
                        break

        elif concert.genre == "Metal":
            for guitarist in guitarists:
                if "play metal" not in guitarist.skills:
                    flag = True
                    break
            if not flag:
                for singer in singers:
                    if "sing low pitch notes" not in singer.skills:
                        flag = True
                        break
            if not flag:
                for drummer in drummers:
                    if "play the drums with drumsticks" not in drummer.skills:
                        flag = True
                        break

        elif concert.genre == "Jazz":
            for guitarist in guitarists:
                if "play jazz" not in guitarist.skills:
                    flag = True
                    break
            if not flag:
                for singer in singers:
                    if "sing low pitch notes" not in singer.skills and "sing high pitch notes" not in singer.skills:
                        flag = True
                        break
            if not flag:
                for drummer in drummers:
                    if "play the drums with drum brushes" not in drummer.skills:
                        flag = True
                        break

        if flag:
            raise Exception(f"The {band.name} band is not ready to play at the concert!")

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")

        musician = self.get_musician_by_name(name)
        if musician:
            raise Exception(f"{name} is already a musician!")

        musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(musician)

        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band = self.get_band_by_name(name)
        if band:
            raise Exception(f"{name} band is already created!")

        band = Band(name)
        self.bands.append(band)

        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert = self.get_concert_by_place(place)
        if concert:
            raise Exception(f"{place} is already registered for {concert.genre} concert!")

        concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(concert)

        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):
        musician = self.get_musician_by_name(musician_name)
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = self.get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band.members.append(musician)

        return f"{musician.name} was added to {band.name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = self.get_band_by_name(band_name)
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        musician_in_band = self.get_musician_by_name_in_a_band(musician_name, band)
        if not musician_in_band:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")

        band.members.remove(musician_in_band)

        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self.get_band_by_name(band_name)
        band_members = {"Guitarist": 0,
                        "Drummer": 0,
                        "Singer": 0}

        for member in band.members:
            if member.__class__.__name__ in band_members:
                band_members[member.__class__.__name__] += 1

        if band_members["Guitarist"] < 1 or band_members["Drummer"] < 1 or band_members["Singer"] < 1:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")

        concert = self.get_concert_by_place(concert_place)
        guitarists = [m for m in band.members if m.__class__.__name__ == "Guitarist"]
        singers = [m for m in band.members if m.__class__.__name__ == "Singer"]
        drummers = [m for m in band.members if m.__class__.__name__ == "Drummer"]

        self.members_can_play_at_concert(concert, guitarists, singers, drummers, band)

        profit = (concert.audience * concert.ticket_price) - concert.expenses

        return f"{band.name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."



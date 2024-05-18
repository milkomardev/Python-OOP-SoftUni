from typing import List
from project.player import Player
from project.supply.supply import Supply


class Controller:
    VALID_SUPPLIES = ("Food", "Drink")

    def __init__(self):
        self.players: List[Player] = []
        self.supplies: List[Supply] = []

    def add_player(self, *new_players):
        successfully_added = []

        for new_player in new_players:
            if new_player not in self.players:
                self.players.append(new_player)
                successfully_added.append(new_player.name)

        return f"Successfully added: {', '.join(successfully_added)}"

    def add_supply(self, *new_supplies):
        [self.supplies.append(s) for s in new_supplies]

    def sustain(self, player_name: str, supply_type: str):
        if supply_type not in self.VALID_SUPPLIES:
            return

        current_player = [p for p in self.players if p.name == player_name][0]

        if not current_player:
            return

        if not current_player.need_sustenance:
            return f"{player_name} have enough stamina."

        for i in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[i]

            if supply.__class__.__name__ == supply_type:
                self.supplies.pop(i)
                break
        else:
            raise Exception(f"There are no {supply_type.lower()} supplies left!")

        current_player.stamina = min(100, current_player.stamina + supply.energy)

        return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):

        first_p = [p for p in self.players if p.name == first_player_name][0]
        second_p = [p for p in self.players if p.name == second_player_name][0]
        players = [first_p, second_p]
        result = []

        for p in players:
            if p.stamina == 0:
                result.append(f"Player {p.name} does not have enough stamina.")

        if result:
            return '\n'.join(result)

        first_attacker = first_p if first_p.stamina < second_p.stamina else second_p
        second_attacker = second_p if first_p.stamina < second_p.stamina else first_p

        second_attacker.stamina = max(0, second_attacker.stamina - first_attacker.stamina / 2)
        if second_attacker.stamina == 0:
            return f"Winner: {first_attacker.name}"

        first_attacker.stamina = max(0, first_attacker.stamina - second_attacker.stamina / 2)
        if first_attacker.stamina == 0:
            return f"Winner: {second_attacker.name}"

        if first_attacker.stamina > second_attacker.stamina:
            return f"Winner: {first_attacker.name}"

        return f"Winner: {second_attacker.name}"

    def next_day(self):
        for p in self.players:
            p.stamina = max(0, p.stamina - p.age*2)

            self.sustain(p.name, "Food")
            self.sustain(p.name, "Drink")

    def __str__(self):
        return '\n'.join([str(p) for p in self.players] + [s.details() for s in self.supplies])

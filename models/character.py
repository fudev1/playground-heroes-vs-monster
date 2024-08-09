from models.weapon import *
from utils.colors import *

class Character:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health
        self.max_health = health

        self.weapon = poings

    def attack(self, target):
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        print(f"{color_blue3}{self.name}{color_default} "
              f"a fait {color_red}{self.weapon.damage}{color_default} points de dégâts "
              f"à {color_blue3}{target.name}{color_default} avec {color_green1}{self.weapon.name}{color_default}")



class Hero(Character):
    def __init__(self, name: str, health: int):
        super().__init__(name, health)


class Enemy(Character):
    def __init__(self, name: str, health: int, weapon):
        super().__init__(name, health)
        self.weapon = weapon

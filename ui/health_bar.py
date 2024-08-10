
from utils import *

class HealthBar:
    symbol_remaining: str = "█"
    symbol_lost: str = "▄"

    def __init__(self, entity, length: int, is_colored: bool = True, color: str = ""):
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health


        self.is_colored = is_colored
        self.color = color if color else ""

    def update(self):
        self.current_value = self.entity.health

    def draw(self):
        reamining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - reamining_bars
        print(f"{self.entity.name} : {self.enttiy.health} / {self.max_value}")

        print(f"{self.color}"
              f"{reamining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}")

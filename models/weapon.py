class Weapon:
    def __init__(self, name: str, weapon_type: str, damage: int, value: int):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


epee_mousse = Weapon(name="Epée en Mousse", weapon_type="corps à corps", damage=5, value=10)

arc_court = Weapon(name="Arc court", weapon_type="distance", damage=3, value=5)

poings = Weapon(name="Poings", weapon_type="emoussé", damage=20, value=5)

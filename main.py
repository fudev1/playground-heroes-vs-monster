from ui.status_bars import display_health_mana
from models.character import Hero, Enemy, Character
from models.weapon import arc_court, poings, epee_mousse

def main():


    hero = Hero(name="🧙 Hero", health=100)
    hero.equip(epee_mousse)
    troll = Enemy(name="🧌  Troll", health=100, weapon=arc_court)

    while True:
        hero.attack(troll)
        troll.attack(hero)

        print(f"\n🔸vie du {hero.name} : [{hero.health}]")
        print(f"🔸vie du {troll.name} : [{troll.health}]\n")
        hero.drop()


        print("\n--------------------------------------------------------------------------------")
        input("")



if __name__ == '__main__':
    main()

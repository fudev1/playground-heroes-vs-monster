from ui.status_bars import display_health_mana
from models.character import Hero, Enemy, Character
from models.weapon import arc_court, poings, epee_mousse

def main():
    # # Init valeur santé/mana

    # max_health = 100
    # current_health = 80

    # max_mana = 100
    # current_mana = 100


    # # Appel de la fonction
    # display_health_mana(current_health, max_health, current_mana, max_mana)


    # # Simulation
    # while True:
    #     input("")
    #     current_health -= 5
    #     current_mana -= 9

    #     current_health = max(0, current_health)
    #     current_mana = max(0, current_mana)

    #     display_health_mana(current_health, max_health, current_mana, max_mana)

    #     if current_health <= 0:
    #         print("\nGame over!\n")
    #         break



    hero = Hero(name="Hero", health=100)
    monster = Enemy(name="Monster", health=100, weapon=arc_court)

    while True:
        hero.attack(monster)
        monster.attack(hero)

        print(f"\n🔸vie du {hero.name} : {hero.health}")
        print(f"🔸vie du {monster.name} : {monster.health}")
        print("\n--------------------------------------------------------------------------------")
        input("")




if __name__ == '__main__':
    main()

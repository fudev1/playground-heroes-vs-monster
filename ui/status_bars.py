# ascii art
# █ ▓ ▒ ░
# Gestion barre de vie et mana

from utils import *

def display_health_mana(current_health, max_health, current_mana, max_mana):
    bars = 20
    remaining_health_symbol = "▄"
    lost_health_bars_symbol = "▄"

    remaining_health_bars = round(current_health / max_health * bars)
    lost_health_bars = bars - remaining_health_bars

    remaining_mana_bars = round(current_mana / max_mana * bars)
    lost_mana_bars = bars - remaining_mana_bars


    # update color `santé`
    if current_health > 0.66 * max_health:
        health_color = color_green1
    elif current_health > 0.33 * max_health:
        health_color = color_yellow
    else:
        health_color = color_red


    # Affichage barre de santé
    print(f"VIE: {current_health} / {max_health}")
    print(f"{health_color}{remaining_health_bars * remaining_health_symbol}{color_default}"
          f"{dark_gray}{lost_health_bars * lost_health_bars_symbol}{color_default}")

    print(" ")

    # Affichage barre de mana
    print(f"MANA: {current_mana} / {max_mana}")
    print(f"{color_blue1}{remaining_mana_bars * remaining_health_symbol}"
          f"{dark_gray}{lost_mana_bars * lost_health_bars_symbol}{color_default}")

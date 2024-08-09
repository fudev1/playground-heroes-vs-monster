# ascii art
# █ ▓ ▒ ░

from utils import *


# Définir la Santé
max_health = 100
current_health = 80

max_mana = 100
current_mana = 100

bars = 20

remaining_health_symbol = "▄"
lost_health_bars_symbol = "▄"

health_color = color_green1



while True:

    remaining_health_bars = round(current_health / max_health * bars)
    lost_health_bars = bars - remaining_health_bars


    remaining_mana_bars = round(current_mana / max_mana * bars)
    lost_mana_bars = bars - remaining_mana_bars


    # Barre de santé restante (moyenne sur 20)
    print(f"VIE: {current_health} / {max_health}")
    print(f"{health_color}{remaining_health_bars * remaining_health_symbol}{color_default}"
          f"{dark_gray}{lost_health_bars * lost_health_bars_symbol}{color_default}")

    print(" ")

    print(f"MANA: {current_mana} / {max_mana}")
    print(f"{color_blue1}{remaining_mana_bars * remaining_health_symbol}"
          f"{dark_gray}{lost_mana_bars * lost_health_bars_symbol}{color_default}")

    input("")
    current_health -= 5
    current_mana -= 9


    current_health = max(0, current_health)
    current_mana = max(0, current_mana)


    # Update couleur `santé`
    if current_health > 0.66 * max_health:
        health_color = color_green1
    elif current_health > 0.33 * max_health:
        health_color = color_yellow
    else:
        health_color = color_red

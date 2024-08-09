# ascii art
# █ ▓ ▒ ░



# Définir la Santé
max_health = 100
current_health = 80
bars = 20

remaining_health_symbol = "█"
lost_health_bars_symbol = "░"



while True:
    # Barre de santé restante (moyenne sur 20)
    remaining_health_bars = round(current_health / max_health * bars)
    lost_health_bars = bars - remaining_health_bars


    print(f"HEALTH: {current_health} / {max_health}")
    print(f"|{remaining_health_bars * remaining_health_symbol}{lost_health_bars * lost_health_bars_symbol}|")
    input("")
    current_health -= 5

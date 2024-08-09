# utility pour afficher les couleurs

symbol = "█"

color_red = "\033[91m"
color_purple = "\033[95m"
color_blue1 = "\033[34m"
color_blue2 = "\033[36m"
color_blue3 = "\033[96m"
color_green1 = "\033[92m"
color_green2 = "\033[32m"
color_brown = "\033[33m"
color_gray = "\033[37m"
color_yellow = "\033[93m"
color_default = "\033[0m"
color_list = ( color_red, color_purple, color_blue1, color_blue2, color_blue3, color_green1, color_green2, color_brown, color_gray, color_yellow, color_default )


# affiche le nom de la variable
def print_colored(variable):
    for name, value in globals().items():
        if id(value) == id(variable):
            return name


# affiche les couleurs
def show_colors():
    for color in color_list:
        print(f"{color}{3 * symbol}", end="")

    print(color_default)

    for color in color_list:
        print(f"{color}{3 * symbol} {print_colored(color)}")

    input("")

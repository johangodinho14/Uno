from modules.menu import Menu
from modules.system import System

class Inputs:
    '''
    About - Includes all functions relating to various inputs:
        * Get_wild_card_color - Get's user input and returns value, includes validation

    Dependencies:
        * Internal - Menu
        * Internal - System

    '''
    def __init__(self):
        self.__menu   = Menu()
        self.__system = System()
        pass

    def get_wild_card_color(self):
        colors    = {}


        card_colors = self.__system.parse_config()[-2]
        for i in range(0,len(card_colors)):
            colors[str(i+1)] = card_colors[i]

        #Getting user input re: wild card colour
        self.__menu.show_color_menu()
        selected_color = input(str("Please select a color : "))

        while 1:
            if selected_color == "1" or selected_color == "2" or selected_color == "3" or selected_color == "4":
                return colors[selected_color]
            else:
                selected_color = input(str("Please select a color : "))

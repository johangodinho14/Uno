from modules.menu import Menu
from modules.system import System

class Inputs:
    '''
    About - Includes all functions relating to various inputs:
        * Add                      - Add cards to the card
        * Get_cards                - Returns all cards in the player hand
        * Transfer_card            - Moves / Transfers a given card from the player hand to the main deck
        * Show_cards               - Displays / Prints all the cards in a player's hand
        * Set_wild_card_color      - Finds wild card and changes its color to the given argument / parameter
        * Use_card                 - checks if a player is allowed to use a card, if true it uses the card else it pulls a card from the deck to player hand
        * Check_for_matching_cards - checks the player / computer hand for a card that matches the top card of the deck

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

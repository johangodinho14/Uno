from colorama import Fore, Back, Style
from modules.menu import Menu

class Player:
    def __init__(self):
        self.__menu = Menu()
        pass

    def get_wild_card_color(self):
        colors    = {
            "1":"RED",
            "2":"GREEN",
            "3":"BLUE",
            "4":"YELLOW",
        }

        self.__menu.show_color_menu()
        selected_color = input(str("Please select a color : "))

        while 1:
            if selected_color == "1" or selected_color == "2" or selected_color == "3" or selected_color == "4":
                return colors[selected_color]
            else:
                selected_color = input(str("Please select a color : "))


    def hit_card(self,card_index,deck,hand):
        selected_card = hand.get_cards()[card_index]

        #Check if the selected card matches the top card of the deck (match = either number or colors match)
        check_result = deck.match(selected_card)
        match_check  = check_result['match']
        wild_check   = check_result['wild']

        #Checking if the card matched or a wild card was used
        if wild_check == True and match_check == True:
            wild_card_color  = self.get_wild_card_color()
            hand.set_wild_card_color(wild_card_color)
            hand.transfer_card(selected_card,deck)

        #Checking if the player's card matched the top card of the deck
        if match_check == True and wild_check == False:
            hand.transfer_card(selected_card,deck)
        
        #Player's card wasn't a wild card and didn't match the top card of the deck
        if match_check == False and wild_check == False:
            print(Fore.RED+"You cannot use this card, Please pull a card from the deck."+Fore.GREEN)
            return False


from colorama import Fore
import time
from modules.inputs import Inputs

class Hand:
    '''
    About - Includes all functions relating to a player hand (cards a player has):
        * Add                   - Add cards to the card
        * Get_cards             - Returns all cards in the player hand
        * Transfer_card         - Moves / Transfers a given card from the player hand to the main deck
        * Show_cards            - Displays / Prints all the cards in a player's hand
        * Set_wild_card_color   - Finds wild card and changes its color to the given argument / parameter

    Dependencies:
        * External - Colorama
        * Internal - Inputs
    '''

    def __init__(self):
        self.__cards     = []
        self.__inputs    = Inputs()

    #Add card to player hand
    def add(self,cards):
        for card in cards:
            self.__cards.append(card)

    #View all cards in player hand
    def get_cards(self):
        return self.__cards
    
    #Removes card from player hand and transfers it back to the deck    
    def transfer_card(self,card,deck):
        if len(self.__cards) > 0:
            self.__cards.remove(card)
            deck.add(card)
        else:
            print("Hand has no cards")

    #Shows cards the player currently has
    def show_cards(self):
        player_cards = self.get_cards()

        print("Your Card count     : "+str(len(player_cards)),"\n")

        print(20*"-" + " Player Cards " + 20*"-" + "\n")
        
        for i in range(0,len(player_cards)):
            card = player_cards[i]
            card_color, card_type, card_id = card.get_properties()
            print(" ["+str(i+1)+"] "+card_id)

        print("")
        print(54*"-")

    def set_wild_card_color(self,color,card_index):
        self.__cards[card_index].set_color(color)

        

    def use_card(self,card_index,deck):
        selected_card = self.get_cards()[card_index]

        #Check if the selected card matches the top card of the deck (match = either number or colors match)
        check_result = deck.match(selected_card)
        match_check  = check_result['match']
        wild_check   = check_result['wild']

        #Checking what combination of cards was satisfied if any
        if wild_check == True and match_check == True:
            wild_card_color  = self.__inputs.get_wild_card_color()
            self.set_wild_card_color(wild_card_color,card_index)
            self.transfer_card(selected_card,deck)

        if match_check == True and wild_check == False:
            self.transfer_card(selected_card,deck)

        if match_check == False and wild_check == False:
            if self.check_for_matching_cards(deck.get_top_card()) == True:
                print(Fore.RED+"You cannot use this card"+Fore.YELLOW)
                time.sleep(1)
                return True
            else:
                print(Fore.RED+"You don't have any matching cards, A card will be pulled from the deck"+Fore.YELLOW)
                deck.draw(self,amount=1)
                time.sleep(1)
                return False
            

    def check_for_matching_cards(self,top_card):
        for card in self.__cards:
            card_type = card.get_properties()[-2]
            card_color= card.get_properties()[-3]
            
            if card_type == "WILD" or card_type ==  top_card.get_properties()[-2] or card_color == top_card.get_properties()[-3]:
                    return True
                    
        return False



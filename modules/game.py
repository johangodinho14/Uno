from colorama import Fore
from modules.deck import Deck
from modules.hand import Hand
from modules.system import System

class Game:
    '''
    About - Includes all functions relating to the game:
        * Init game             - Runs's all functions required to initialise a game
        * Get computer hand     - Returns all cards in the computer hand
        * Get player hand       - Returns all cards in the player hand
        * Get deck              - Returns deck 
        * Show player stats     - Displays count of player and computer cards and displays all cards in player hand
        * Get turn              - Returns Integer representing who's turn it is i:e (1 = Player 2 = Computer)
        * Next turn             - Switches from current player turn to next player turn
        * Top card used         - Setter - Allows status of the top card to be set with regards to whether it has already been used
        * Get top card status   - Getter - Gets status of whether the top card has already been used (mainly if it was a power card)
        * Handle power card     - Handles all actions relating to the power cards played e.g. reverse, draw, skip, etc.
        * Check_win             - Checks if the game by verifying if any of the players have an empty hand
        
    
    Dependencies:
        * Internal module - Deck
        * Internal module - Hand
        * Internal module - System
    '''

    def __init__(self,initial_cards):
        self.__deck          = Deck()
        self.__computer_hand = Hand()
        self.__player_hand   = Hand()
        self.__system        = System()
        self.__turn          = 1  # 1 = Player 2 = Computer
        self.__initial_cards = initial_cards
        self.__top_card_used = False

    def init_game(self):
        # Starting the game
        self.__deck = Deck()
        self.__deck.populate_deck()
        self.__deck.shuffle()

        # Hands (Computer and Player)
        self.__computer_hand = Hand()
        self.__player_hand   = Hand()

        # Serving cards to players
        self.__deck.draw(
            self.__computer_hand,
            amount=self.__initial_cards
        )
        self.__deck.draw(
            self.__player_hand,
            amount=self.__initial_cards
        )
    
    def get_computer_hand(self):
        return self.__computer_hand
    
    def get_player_hand(self):
        return self.__player_hand

    def get_deck(self):
        return self.__deck

    def show_player_stats(self):
        #Clearing sceen and showing top card and computer card count
        self.__system.clear_screen()
        
        print(Fore.LIGHTRED_EX+"\nTop card            : " + self.__deck.get_top_card().get_properties()[-1])    
        print("Computer card count : "   + str(len(self.__computer_hand.get_cards())))
        print("Deck card count     : "   + str(len(self.__deck.get_cards())))

        self.__player_hand.show_cards()

    def get_turn(self):
        return self.__turn
    
    def next_turn(self):
        if self.__turn == 2:
            self.__turn = 1
        else:
            self.__turn = 2

    def top_card_used(self,status):
        self.__top_card_used = status
    
    def get_top_card_status(self):
        return self.__top_card_used

    def handle_power_card(self):
        card_type = self.__deck.get_top_card().get_properties()[-2]
        if card_type == "REVERSE" and self.get_top_card_status() == False:
            self.next_turn()
            self.next_turn()
        
        elif card_type == "DRAW 2" and self.get_top_card_status() == False:
            if self.get_turn() == 1:
                self.__deck.draw(self.__computer_hand,amount=2)
            else:
                self.__deck.draw(self.__player_hand,amount=2)

        elif card_type == "DRAW 4" and self.get_top_card_status() == False:
            if self.get_turn() == 1:
                self.__deck.draw(self.__computer_hand,amount=4)
            else:
                self.__deck.draw(self.__player_hand,amount=4)

        elif card_type == "SKIP" and self.get_top_card_status() == False:
            self.next_turn()
            self.next_turn()
        
        else:
            self.next_turn()

        #If the top card isn't a wild card we make sure all wild cards in the deck are resetted to black
        if card_type != "WILD":                    
             self.__deck.reset_wild_card_color()
    
    def check_win(self):
        if len(self.__computer_hand.get_cards()) == 0 and len(self.__player_hand.get_cards()) == 0:
            return {"game_over":True, "winner":"Draw"}
        elif len(self.__computer_hand.get_cards()) == 0:
            return {"game_over":True, "winner":"Computer"}
        elif len(self.__player_hand.get_cards()) == 0:
            return {"game_over":True, "winner":"Player"}
        else:
            return {"game_over":False, "winner":None}

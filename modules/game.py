from modules.deck import Deck
from modules.hand import Hand
from modules.system import System

class Game:
    def __init__(self,initial_cards):
        self.__deck          = Deck()
        self.__computer_hand = Hand()
        self.__player_hand   = Hand()
        self.__system        = System()
        self.__turn          = 1  # 1 = Player 2 = Computer
        self.__initial_cards = initial_cards
        pass

    def init_game(self):
        # Starting the game
        self.__deck = Deck()
        self.__deck.populate_deck()
        self.__deck.shuffle()

        print(self.__deck.get_top_card().get_properties())

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
        
        print("\nTop card            : " + self.__deck.get_top_card().get_properties()[-1])    
        print("Computer card count : "   + str(len(self.__computer_hand.get_cards())))

        self.__player_hand.show_cards()

    def get_turn(self):
        return self.__turn
    
    def next_turn(self):
        if self.__turn == 2:
            self.__turn = 1
        else:
            self.__turn = 2
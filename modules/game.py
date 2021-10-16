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

    def handle_power_card(self):
        card_type = self.__deck.get_top_card().get_properties()[-2]
        if card_type == "REVERSE":
            self.next_turn()
            self.next_turn()
        
        elif card_type == "DRAW 2":
            if self.get_turn() == 1:
                self.__deck.draw(self.__player_hand,amount=2)
            else:
                self.__deck.draw(self.__computer_hand,amount=2)

        elif card_type == "DRAW 4":
            if self.get_turn() == 1:
                self.__deck.draw(self.__player_hand,amount=4)
            else:
                self.__deck.draw(self.__computer_hand,amount=4)
        
        elif card_type == "WILD":
            self.__deck.reset_wild_card_color()
        
        else:
            self.next_turn()
        

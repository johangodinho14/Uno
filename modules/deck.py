import random
from modules.system import System
from modules.card   import Card

class Deck:
    '''
    About - Includes all functions relating to the deck:
        * Add           - Add a card to the deck
        * Populate_deck - Uses class (Card) to populate the deck with cards, based on the `config.js` file
        * Draw          - Draw (amount) number of cards from the deck and deposit them into the player hand (cards)
        * Get_top_card  - Returns the top card of the deck
        * Get_cards     - Returns the deck (list)
        * Shuffle       - Shuffles all cards in the deck (list)
        * Match         - Matches player card to the card at the top of the deck, includes handle for Wild card
    
    Dependencies:
        * Internal module - System
        * Internal module - Card
        * External module - random
    '''

    def __init__(self):
        self.__deck        = []
        self.__system      = System()
    
    #Add a card to the deck
    def add(self,card):
        self.__deck.append(card)

    #Uses Class Card to create an instance of card for each card color and card type present in config 
    #Populates deck with cards
    def populate_deck(self):
        meta_data   = self.__system.parse_config()
        card_colors, card_types = meta_data
        
        for card_color in card_colors:
            #Adding wild card to the deck 
            self.add(Card("BLACK","WILD"))
            
            for card_type in card_types:
                card        = Card(card_color,card_type)
                self.add(card)
    
    #Draw a given (amount) -> int of cards from the deck and them add them to the player hand provided
    def draw(self,player_hand,amount=1):
        if amount > len(self.__deck):
            print("Not enough cards in the deck to draw.")
            return

        drawn_cards = []
        for i in range(0,amount):
            random_card_index = random.randint(0,len(self.__deck)-1)
            random_card       = self.__deck[random_card_index]

            drawn_cards.append(random_card)
            self.__deck.remove(random_card)

        player_hand.add(drawn_cards)

    #Get the properties of the card on the top of the deck
    def get_top_card(self):
        return self.__deck[-1]

    #Get a list of cards available in the deck (list)
    def get_cards(self):
        return self.__deck
    
    #Shuffle the cards in the deck (list)
    def shuffle(self):
        random.shuffle(self.__deck)
        
    #Check if the card player has hit matches the top card of the deck
    def match(self,card):
        top_card_color, top_card_type, top_card_id          = self.get_top_card().get_properties()
        player_card_color, player_card_type, player_card_id = card.get_properties()

        #Conditions based on which the user can hit the selected card 
        if top_card_color == player_card_color or top_card_type == player_card_type:
            return {"match":True,"wild":False}
        elif player_card_type == "WILD":
            return {"match":True,"wild":True}
        else:
            return False

import random

class Deck:
    '''
    About - Includes all functions relating to the deck:
        * Add          - Add a card to the deck
        * Draw         - Draw (amount) number of cards from the deck and deposit them into the player hand (cards)
        * Get_top_card - Returns the top card of the deck
        * Get_cards    - Returns the deck (list)
        * Shuffle      - Shuffles all cards in the deck (list)
    '''

    def __init__(self):
        self.deck        = []
    
    #Add a card to the deck
    def add(self,card):
        self.deck.append(card)
    
    #Draw a given (amount) -> int of cards from the deck and them add them to the player hand provided
    def draw(self,player_hand,amount=1):
        if amount > len(self.deck):
            return "Not enough cards in the deck to draw."

        drawn_cards = []
        for i in range(0,amount):
            random_card_index = random.randint(0,len(self.deck)-1)
            random_card       = self.deck[random_card_index]

            drawn_cards.append(random_card)
            self.deck.remove(random_card)

        player_hand.add(drawn_cards)

    #Get the properties of the card on the top of the deck
    def get_top_card(self):
        return self.deck[-1]

    #Get a list of cards available in the deck (list)
    def get_cards(self):
        return self.deck
    
    #Shuffle the cards in the deck (list)
    def shuffle(self):
        random.shuffle(self.deck)
        


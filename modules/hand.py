class Hand:
    """
    About - Includes all functions relating to a player hand (cards a player has):
        * Add                   - Add cards to the card
        * Get_cards             - Returns all cards in the player hand
        * Transfer_card         - Moves / Transfers a given card from the player hand to the main deck
    
    Dependencies:
        * None
    """

    def __init__(self):
        self.cards     = []

    #Add card to player hand
    def add(self,cards):
        for card in cards:
            self.cards.append(card)

    #View all cards in player hand
    def get_cards(self):
        return self.cards
    
    #Removes card from player hand and transfers it back to the deck    
    def transfer_card(self,card,deck):
        self.cards.remove(card)
        deck.add(card)

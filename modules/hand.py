class Hand:
    '''
    About - Includes all functions relating to a player hand (cards a player has):
        * Add                   - Add cards to the card
        * Get_cards             - Returns all cards in the player hand
        * Transfer_card         - Moves / Transfers a given card from the player hand to the main deck
        * Show_cards            - Displays / Prints all the cards in a player's hand
        * Set_wild_card_color   - Finds wild card and changes its color to the given argument / parameter

    
    Dependencies:
        * None
    '''

    def __init__(self):
        self.__cards     = []

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

    def set_wild_card_color(self,color):
        #Finding wild card in the deck and setting custom color based on user's choice
        for card in self.__cards:
            if card.get_properties()[-2] == "WILD":
                card.set_color(color)

        
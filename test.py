from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand


colors = ['RED','GREEN','BLUE','YELLOW']
types  = ['0','1','2','3','4','5','6','7','8','9','skip','reverse','draw_2','draw_4','wild']

deck   = Deck()

for color in colors:
    card_color = color
    for card_type in types:
        card = Card(card_color,card_type)
        deck.add(card)

deck.shuffle()

# player_1_hand = Hand()

# print("The deck has ",len(deck.get_cards()))
# print("Player hand has ",len(player_1_hand.get_cards()))

# deck.draw(player_1_hand,10)

# print("The deck has ",len(deck.get_cards()))
# print("Player hand has ",len(player_1_hand.get_cards()))


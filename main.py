#Importing all internal and external modules
from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand
from modules.system import System
from modules.menu   import Menu

#Game variables
player_turn  = 1
game_running = True

#Instantiating classes
menu = Menu()

#Game main loop (Breaks when, game is over)
while game_running:
    menu.show_main_menu()
    menu.show_sub_menu()
    break



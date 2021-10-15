#Importing all internal and external modules
from os import system
from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand
from modules.system import System
from modules.menu   import Menu

#Game variables
player_turn  = 1
game_running = True

#Instantiating classes
menu    = Menu()
system = System()

#Main Game
def start_game():
    # Starting the game
    deck = Deck()
    deck.populate_deck()
    deck.shuffle()

    # Hands (Computer and Player)
    computer_hand = Hand()
    player_hand = Hand()

    # Serving cards to players
    deck.draw(computer_hand,amount=7)
    deck.draw(player_hand,amount=7)
 
    #Clearing sceen and showing top card and computer card count
    system.clear_screen()
    print("\nTop card            : " + deck.get_top_card().get_properties()[-1])    
    print("Computer card count : " + str(len(computer_hand.get_cards())))
    
    #Displaying player hand
    player_hand.show_cards()

    #Showing sub menu to the player
    menu.show_sub_menu()

    #Getting input from player re: his/ her move
    player_action = input(str("\nPlease select an option : "))
    
    while 1:
        if player_action == "1":
            print("yay")
            break
        elif player_action == "2":
            break
        elif player_action == "3":
            break
        else:
            player_action = input(str("Please select an option : "))


    

        
    
    
#Game main loop (Breaks when, game is over)
while game_running:
    menu.show_main_menu()
    menu_option = input(str("\nPlease select an option : "))

    if menu_option == "1":
        start_game()
    elif menu_option =="2":
        start_game()
    elif menu_option == "3":
        game_running = False

        system.clear_screen()
        print("\n Thanks for playing UNO")
        print(" Developed by JJ")
        



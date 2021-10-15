#Importing all internal and external modules
from os import system
from colorama import Fore
from modules.card import Card
from modules.deck import Deck
from modules.hand import Hand
from modules.system import System
from modules.menu   import Menu
from modules.player import Player


#Game variables
player_turn  = 1
game_running = True

#Instantiating classes
menu    = Menu()
system = System()

#Functions


def start_game():
    # Starting the game
    deck = Deck()
    deck.populate_deck()
    deck.shuffle()

    # Hands (Computer and Player)
    computer_hand = Hand()
    player_hand   = Hand()

    # Serving cards to players
    deck.draw(computer_hand,amount=7)
    deck.draw(player_hand,amount=7)

    player = Player()
    
    while 1:
        #Clearing sceen and showing top card and computer card count
        system.clear_screen()
        print("\nTop card            : " + deck.get_top_card().get_properties()[-1])    
        print("Computer card count : " + str(len(computer_hand.get_cards())))
        
        #Displaying player hand
        player_hand.show_cards()

        #Showing sub menu to the player
        menu.show_sub_menu()

        #Getting input from player re: his/ her move
        player_action = input(str(Fore.YELLOW+"\nPlease select an option : "))

        #If player selects to use a card from his/her deck
        if player_action == "1":
            while 1:
                #Error handling to ensure the user only enters a number
                try:
                    selected_card_index = int(input(Fore.YELLOW+"Please select a card    : "))
                    if selected_card_index <= len(player_hand.get_cards()):
                        #Checking if the player should be able to select a card again
                        if player.hit_card(selected_card_index-1,deck,player_hand) != False:
                            player_action = ""
                            break

                    else:
                        print(Fore.RED+"No such card exists"+Fore.YELLOW)
                
                except ValueError as e:
                    print(Fore.RED+"Input needs to be a number"+Fore.YELLOW)       
        
        elif player_action == "2":
            break
        elif player_action == "3":
            break
        else:
            pass



#Game main loop (Breaks when, game is over)
while game_running:
    menu.show_main_menu()
    menu_option = input(str(Fore.YELLOW+"\nPlease select an option : "))

    if menu_option == "1":
        start_game()
    elif menu_option =="2":
        start_game()
    elif menu_option == "3":
        game_running = False

        system.clear_screen()
        print("\n Thanks for playing UNO")
        print(" Developed by JJ")
        



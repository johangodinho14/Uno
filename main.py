#Importing all internal and external modules
import sys
import time
from colorama import Fore
from modules.system import System
from modules.menu   import Menu
from modules.game   import Game
from modules.computer import Computer

#Instantiating classes
menu        = Menu()
system      = System()
computer    = Computer()

def computer_turn(deck,computer_hand,game):
    print("\nComputer is thinking...")
    time.sleep(1.5)

    computer_move_response = computer.check_move(deck,computer_hand)
    computer_move = computer_move_response['move']
    computer_card = computer_move_response['card']

    if computer_move == "use_card":
        print("\nComputer used : ", computer_card.get_properties()[-1])
        computer_hand.transfer_card(computer_card,deck)
        game.top_card_used(False)
        input("Press enter to continue")
    else:
        game.top_card_used(True)
        print("\nComputer drew a card from the deck")
        deck.draw(computer_hand,amount=1)
        input("Press enter to continue")

def player_turn(game,deck,player_hand):
    #Displaying Player Stats and Sub-Menu
    game.show_player_stats()
    menu.show_sub_menu()

    #Getting input from player re: his/ her move
    player_action = input(str(Fore.YELLOW+"\nPlease select an option : "))

    #Options -> Use card
    if player_action == "1":
        while 1:
            #Error handling to ensure the user only enters a number
            try:
                selected_card_index = int(input(Fore.YELLOW+"Please select a card    : "))
                if selected_card_index <= len(player_hand.get_cards()):
                        #Returns true if player has a card that can be used 
                        use_hand_status = player_hand.use_card(selected_card_index-1,deck)

                        if  use_hand_status == True:
                            continue
                        elif use_hand_status == None:
                            game.top_card_used(False)
                            player_action = ""
                            game.show_player_stats()
                            input("\nPress Enter to continue")
                            break
                        else:
                            game.top_card_used(True)
                            player_action = ""
                            game.show_player_stats()
                            input("\nPress Enter to continue")
                            break

                else:
                    print(Fore.RED+"No such card exists"+Fore.YELLOW)
                    time.sleep(2)
            
            except ValueError as e:
                print(Fore.RED+"Input needs to be a number"+Fore.YELLOW)       
                time.sleep(2)

    #Options -> Draw card
    elif player_action == "2":
        if len(deck.get_cards())>1:
            game.top_card_used(True)
            deck.draw(player_hand=player_hand,amount=1)
            game.show_player_stats()
            print("\n You drew a card")
            input("\n Press enter to continue")
            
        else:
            print(Fore.RED+"You cannot draw any more cards"+Fore.YELLOW)
            time.sleep(2)
        
    elif player_action == "3":
        main_menu()
    else:
        player_turn(game,deck,player_hand)

#Functions
def start_game():   
    #Initialising the game
    game                 = Game(initial_cards=7)
    game.init_game()
    deck                 = game.get_deck()
    player_hand          = game.get_player_hand()
    computer_hand        = game.get_computer_hand()
    game_status_response = game.check_win()
    game_over            = game_status_response['game_over']
    winner               = game_status_response['winner']

    while game_over != True:
        turn = game.get_turn()

        if turn == 1:
            player_turn(game=game,deck=deck,player_hand=player_hand)

        else:
            computer_turn(deck=deck,computer_hand=computer_hand,game=game)
        
        game.handle_power_card()

    print(Fore.GREEN+"We have a winner !!!"+winner)
    time.sleep(10)

def main_menu():
    menu.show_main_menu()
    menu_option = input(str(Fore.YELLOW+"\nPlease select an option : "))

    if menu_option == "1":
        start_game()
    elif menu_option =="2":
        start_game()
    elif menu_option == "3":
        system.clear_screen()
        print("\n Thanks for playing UNO")
        print(" Developed by JJ")
        sys.exit()
        
    else:
        main_menu()

main_menu()

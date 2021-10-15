#Importing all internal and external modules
from os import system
from colorama import Fore
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

#Functions
def hit_card(card_index,deck,hand):
    selected_card = hand.get_cards()[card_index]
    #Check if the selected card matches the top card of the deck (match = either number or colors match)
    check_result = deck.match(selected_card)
    match_check  = check_result['match']
    wild_check   = check_result['wild']

    #Checking if the card matched or a wild card was used
    if wild_check == True:
        pass
    if match_check == True:
        hand.transfer_card(selected_card,deck)
    else:
        print(Fore.RED+"You cannot use this card, Please pull a card from the deck."+Fore.GREEN)
        return False

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
    
    while 1:
        #Clearing sceen and showing top card and computer card count
        print(Fore.YELLOW)
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
                    selected_card = int(input(Fore.YELLOW+"Please select a card    : "))
                    if selected_card <= len(player_hand.get_cards()):
                        #Checking if the player should be able to select a card again
                        if hit_card(selected_card-1,deck,player_hand) != False:
                            player_action = ""
                            break

                    else:
                        print(Fore.RED+"No such card exists"+Fore.GREEN)
                
                except ValueError as e:
                    print(Fore.RED+"Input needs to be a number"+Fore.GREEN)       
        
        elif player_action == "2":
            break
        elif player_action == "3":
            break
        else:
            player_action = input(str(Fore.YELLOW+"Please select an option : "))


    

        
    
    
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
        



from colorama import Fore, Style, init
from modules.system import System

class Menu:
    '''
        About - Utilities related to the Game Menu's 
            * Show_main_menu  - Displays Main Menu
            * Show_sub_menu   - Displays Sub Menu

         Dependencies:
            * External module - Colorama
            * Internal module - System
    '''

    def __init__(self):
        self.__system = System()
        init(convert=True)
    
    def show_main_menu(self):
        self.__system.clear_screen()
        string = "\n"
        string += 20*"-" + " UNO Main Menu " + 20*"-" + "\n\n" 
        string += " [1] Start Game (Player V Computer) \n"
        string += " [2] Restart Game \n"
        string += " [3] Quit Game\n\n"
        string += 55*"-"

        print(Fore.YELLOW)
        print(string)
       
    def show_sub_menu(self):
        string = "\n"
        string += 20*"-" + " UNO Sub Menu " + 20*"-" + "\n\n" 
        string += " [1] Use a card from your deck \n"
        string += " [2] Pull a card from the deck \n"
        string += " [3] Quit to main menu\n\n"
        string += 54*"-"

        print(Fore.GREEN)
        print(string)

    


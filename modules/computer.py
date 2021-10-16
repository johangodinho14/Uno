import random
from modules.system import System


class Computer:

    def __init__(self):
        self.__system = System()
        pass
    
    def check_move(self,deck,computer_hand):
        use_card  = False
        
        for i in range(0,len(computer_hand.get_cards())):
            computer_card = computer_hand.get_cards()[i]
            match_result  = deck.match(computer_card)

            if match_result['match'] == True or match_result['wild'] == True:
                use_card = True
                break
            else:
                use_card = False

        if use_card == True and match_result['wild'] == True:
            available_colors = self.__system.parse_config()[-2]
            selected_color   = random.choice(available_colors)
            computer_hand.set_wild_card_color(selected_color,i)
            
            return {"move":"use_card","card":computer_card}

        elif use_card == True:
            return {"move":"use_card","card":computer_card} 
        
        else:
            return {"move":"pull_card"}


            
                


  

    
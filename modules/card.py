class Card:
    '''
        About - Holds details relating to the color and type of various cards included in UNO
        Input :
            1. color -> string representing color of the card
            2. type_ -> string representing type_ of the card

        Output : 
            Getter (properties) -> Properties of the card will be returned if method is called
    '''
    
    def __init__(self,color,type_=None):    
        self.color = color
        self.type  = type_
        self.id    = self.color + " " + self.type

    def get_properties(self):
        return self.color, self.type, self.id



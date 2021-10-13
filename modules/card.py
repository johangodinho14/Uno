class Card:
    '''
        About - Holds details relating to the color and type of various cards included in UNO
        Input :
            1. color -> string representing color of the card
            2. type_ -> string representing type_ of the card

        Output : 
            Getter (properties) -> Properties of the card will be returned if method is called
        
        Dependencies:
            * None
    '''
    
    def __init__(self,color,type_=None):    
        self.__color = color
        self.__type  = type_
        self.__id    = self.__color + " " + self.__type

    def get_properties(self):
        return self.__color, self.__type, self.__id



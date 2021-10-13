import json

class System:
    '''
        About - Utilites provided by the game system 
            * Read_config   - Reads config file and returns the file_ object
            * Parse_config  - Loads in json file and parses it. Returns card_colors (list) and  card_types (list)

         Dependencies:
            * External module - json
    '''

    def __init__(self):
        pass

    def read_config(self):
        try:
            file_ = open("./config.json")
        except FileNotFoundError as e:
            return "Config file could not be found"

        return json.load(file_)

    def parse_config(self):
        config      = self.read_config()
        if config == "Config file could not be found":
            return config
        else:
            card_colors = config['colors']
            card_types  = config['types']
            return card_colors, card_types

   

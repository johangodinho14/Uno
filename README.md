# Uno
Repo for Uno game created using python.

Dependencies / Prerequisite: 
1. Colorama -> Install colrama using `pip install colorama`

Running the game: 
1. Clone the repo using https://github.com/johangodinho14/Uno.git
2. Make sure you have python installed on your system
3. Open terminal and navigate to the `/Uno` folder 
4. Type in `python main.py` and hit enter


## Challenge outline
The challenge picked during this assignment was creating a popular console based game `Uno`. Uno is a card game, where the objective of the game is for the players to lose their cards as soon as possible. The game includes several normal cards along with power cards. I decided to add a bot to the game that is able to play the game with a human player. During the planning stage of the game I discovered potential problems that I would face down the lines, the problems and the potential solutions I thought of have been stated below: 

### Summary of the problem and proposed solution
**Potential problems discovered**
1. Due to the scope of the game being massive, my main goal was to make sure that the code was concise and didn't repeat a lot to ensure simplicity.
2. Since the game includes cards, I wanted to make sure that the cards being used in the game could be changed without having to hard code them into the main code.
3. Due to the different moving bits of the game, I wanted to ensure that there isn't one big file that includes most of the code, as it would become difficult to manage the code.

**Potential Solutions**

Based on the overall problem (challenege) and the potential problems that I discovered during the early planning phases, some of the solutions I planned have been stated below: 
1. Making sure the project follows a modular approach, so that individual elements of the game can be stored in an organised manner in different module files.
2. Making sure the proect followed OOP, to ensure the use of abstraction and simplicity in the main code. This would help increase readability and also ensure that the code can be managed easily.
3. Making sure that the game is able to read a config file that will include default settings of the game, such as the cards that are to be used in the deck

## Initial working plan, overall approach, development strategy and approach to quality

Due to complexity of the card game (Uno) and the given timeline, I decided to use the Agile methodology to ensure that the code was robust and reliable while ensuring that its completed on the given timeline. I began the project by planning all the potential problems and the solutions to them, some of which have already been stated in the section above. The planning phase also included decomposing the overall problems into smaller tasks / epics, this helped me get a definitive list of tasks that need to be completed to complete the overall game on time. 

Once the planning phase was completed, I moved onto the development of the game, I decided to use a modular approach while usign OOP (Object Oriented Programming), to ensure that the code is robust, readable and easily updatable. Once the first sprint of development was completed, I made a list of all the bugs and future features that need to be resolved / added during the next sprint. Using this methodology, I kept evaluating the system in each sprint, until the game was completely functional and meet all the requirements, while not having any bugs.

## Analysis and decomposition of the overall problem into key ‘epic’ style tasks

As I followed the Agile methodology during this project I was able to decompose the overall problem (Uno game) into individual componenets / epic style tasks, these allowed me to have a better overview of all the tasks that needed to be completed before the game could be completed. I took an Object Oriented approach when it came to decomposing the overall problem. I split each element of the game into a class / module of its own so that I could easily create small tasks. Some of the different tasks that the problem was decomposed into have been stated below : 

Task Type | Module name | Short description | Example | 
--- | --- | --- | --- |
Module | Card | Create a class that will have all methods and properties related to a card | get_properties of card |
Module | Deck | Create a class that will have all methods and properties related to a Deck | shuffle, draw_cards, etc. |
Module | Computer | Create a class that will have all methods and properties related to the Computer / Bot | check_move (Decides the move that computer will executed) |
Module | Hand | Create a class that will have all methods and properties related to a Hand | use_card, add_card to hand, show_all_cards in hand |
Module | Inputs | Create a class that will have all methods and properties related to all Inputs | get_wild_card_color (Get's user_input) |
Module | System | Create a class that will have all methods and properties related to the system | read_config, parse_config |
Module | Menu | Create a class that will have all methods and properties relating to the menu | show_main_menu, show_sub_menu |
File | Main | Create a python file that will use all the different modules and set the logic of the game | use of modules such as deck, hand, etc. |

## Initial object-oriented design ideas and planned phased breakdown into smaller tasks 

Due to the overall game already being decomposed into epic style tasks I was able to use the tasks to further explore the various classes that I was going to include within each module. Shown below is a breakdown of the classes that were planned to be created within each module and what they're purpose was.

Module name | Class | Class description | 
--- | --- | --- |
Card | get_properties | Get properties of a selected card, output will include card_color, card_type and card_id |
Card | set_color | Set color of a selected card |
Card | set_color | Set color of a selected card |
Computer | check_move | Depending on the top card of the deck, this method returns whether the computer should draw a card from the deck or play a card from its hand. |
Deck | add | Add a card to the deck |
Deck | populate_deck | Uses class (Card) to populate the deck with cards based onthe the `config.js` file |
Deck | draw | Draw (amount) number of cards from the deck and deposit them into the player hand provided | 
Deck | get_top_card | Returns the top card of the deck | 
Deck | get_cards | Returns the deck as a list | 
Deck | shuffle | Shuffles all the cards in the deck |
Deck | match | Matches player card to the card at the top of the deck, includes handle for Wild card |
Deck | reset_wild_card_color | Finds wild card and resets its color back to black | 
Game | init_game | Runs's all functions required to initialise a new game | 
Game | get_computer_hand | Returns all cards in the computer hand | 
Game | get_player_hand | Returns all cards in the player hand | 
Game | get_deck | Returns deck |
Game | show_player_stats | Displays count of player and computer cards and displays all cards in player hand | 
Game | get_turn | Returns Integer representing who's turn it is i:e (1 = Player 2 = Computer) | 
Game | next_turn | Switches from current player turn to next player turn | 
Game | top_card_used | Setter - Allows status of the top card to be set with regards to whether it has already been used | 
Game | get_top_card_status | Handles all actions relating to the power cards played e.g. reverse, draw, skip, etc. | 
Game | check_win | Checks if the game by verifying if any of the players have an empty hand | 
Game | check_win | Checks if the game by verifying if any of the players have an empty hand | 
Hand | add | Add cards to the hand |
Hand | get_cards | Returns all cards in the player hand | 
Hand | transfer_card | Moves / Transfers a given card from the player hand to the main deck | 
Hand | show_cards | Displays / Prints all the cards in the player hand | 
Hand | set_wild_card_color | Finds wild card in hand and changes its color to the given arg (color) | 
Hand | use_card | Checks if player is allowed to use a card, if true it uses the card else it pull a card from the deck to the player hand | 
Hand | check_for_matching_cards | checks the player / computer hand for a card that matches the top card of the deck | 
Inputs | get_wild_card_color | Get's user input and returns value, includes validation | 
Menu | show_main_menu | Displays Main Menu | 
Menu | show_sub_menu | Displays Sub Menu | 
Menu | show_color_menu | Displays Color Menu on wild card color selection | 
System | read_config | Reads config file and returns the file_ object | 
System | parse_config | Loads in json file and parses it. Returns card_colors (list) and  card_types (list) | 
System | clear_screen | Clears the terminal | 

# Development
## Adoption and use of ‘good’ standards
Throughout the development phase I have tried to use good programming standards throughout the code to make sure that the code is readable, robust and avoids repitition or code smells. Some of the good programming practices that were incorporated in the code were:

1. Standard naming conventions were used (Use of snake_case throughout the project).
2. Pure functions were created where possible to ensure that there were mininmal side effects if the code were to be changed or re-factored in the future.
3. Use of OOP (Object Oriented Programming) was made to ensure that concepts such as abstraction could be used within the code to improve simplicity and readability of the code.
4. The modular programming approach was utilised to split the classes into different files, this helps manage the code in various files and makes it easy to find code snippets and update them when needed.
5. DRY (Don't Repeat Yourself) was used throughout the code to avoid unneccesary duplication of code.
6. Long lines of code with chained commands were avoided 
7. Error handling and validation was added to different parts of the code to ensure that the user isn't allowed to break the program by providing it with invalid data types when prompted for input
8. The use of gloabal variables that keep track of state change was avoided, this was incorportaed as a feature into the `game` class instead.
9. Deep nested loops and conditionals were avoided to keep the logic of the code simple and make it easy to edit in the future.
10. Comments and doc-strings were used within each module to make sure that the code is well documented.

# Phases / Sprints of development 
## Phase 1 + Ensuring Quality through tests and resolving bugs
Phase 1 of development began with the creation of the following modules:
1. Card - This module included the Card class which would help store card details such as (card type and card color), the class also had a getter method which allowed the user to access properties of the card. 
2. Deck - This module was one of the more sophisticated parts of the program due to the fact that it had important properties and methods. All the properties of the class were private so that they could only be accessed from within the Object. Some of the methods that were programmed into the Deck class during this phase included, Shuffle (Shuffles all cards in the deck (list)), Draw card (Draws a card and moves it from the deck to the provided hand) and more.
3. Hand - This module was another important one, since the testing of some of the methods from the Deck class heavily relied on neededing interaction with the Hand class. The Hand class acted as a real life hand that would hold the player and computer cards and have all properties and methods related to the hand, such as Transfer_card (Transfering a card from the hand to the deck), Show_cards (Displaying / Printing all cards in the player hand.)

The 1st phase of development was completing by carrying out various tests on the modules and hte Classes held within them. Some of the tests that were carried out have been displayed in the table below:

Module name | Class | Test description | Expected outcome | Actual outcome | How bugs were resolved | 
--- | --- | --- | --- | --- | --- | 
Card | set_color | Test if the color of the card is changed when the set_color method is used | The colour of the card should be updated | The colour of the card updated | NA | 
Card | get_properties | Test if the properties of the card are returned when the get_properties method is used | The method should return the colour, type and id of the card | The method returned the colour, type and id of the card | NA | 
Deck | add | Test if a given card is added to teh deck when the add method is called| The method should add the given cards to the deck (list)  | The passed card was successfully added to the deck | NA | 
Deck | draw | Test if the draw method is able to draw a given amount of cards from the deck into the given player hand | The method should move the given amount of cards from the deck into the given hand (param / arg)  | This test was partially successfull as the method was able to move the cards to the player hand but it didn't delete the cards from the deck, this caused duplication of cards | I had to ensure that all the cards moved to the player hand were deleted from the deck (list) | 
Deck | match | Test if the match method returns the correct dictionary when a card that isn't a wild card is played | The test should return a dictionary containing {"match":True,"wild":False} when a card matches the top card but isn't a wild card | The method returned {"match":True,"wild":False} when a card matched the top card of the deck and wasn't a wild card | NA | 
Hand | get_cards | Test if all cards in the player hand (list) are returned when the get_cards method is called | The test should return all the cards the player hand currently has | The test returned all the cards in the player hand | NA | 
Hand | set_wild_card_color | Test if the wild card colour is changed to the given colour when the method is called | The colour of the wild card should change and be updated in the player hand | The colour of the wild card was not updated in the player hand  | After going through the code I noticed that the conditional statement that checked the card type had the word "wild" written in lower case instead of upper case which caused the issue of no wild card being detected in the player hand and hence the colour of the wild card was never updated. | 

## Phase 2 + Ensuring Quality through tests and resolving bugs

Phase 2 of development began with the creation of the following modules:

1. System - This module handled all operations related to the system, such as clearing the console, reading and parsing the config file, etc.
2. Menu   - This module handled all operations related to displaying the three different menus that the game had i:e, main menu, sub menu, wild color menu.
3. Inputs - This module handled Input operations and also included validation, it's main job was to handle different input while maintaining validation and returning the output in the end.

The 2nd phase of development was completing by carrying out various tests on the modules and hte Classes held within them. Some of the tests that were carried out have been displayed in the table below:

Module name | Class | Test description | Expected outcome | Actual outcome | How bugs were resolved | 
--- | --- | --- | --- | --- | --- | 
System | read_config | Test if the read_config method returns the `json` config stored in the external file `config.json` | The method should read the data from `config.json` and return a properly structured JSON | The method returned a propertly structured JSON after reading the data from `config.json` | NA | 
System | parse_config | Test if the parse_config method returns a list of card_colors and card_types, read form `config.json`  | The method should return all the card_colors and card_types as lists present in the `config.json` file | The method returned a list of all card_colors and card_types as lists | NA |
Menu | show_main_menu | Test if the method diplays a nicely formatted main menu with all options present | The method should display a nicely formatted menu with all options | The menu did print out the options but the formatting wasn't properly alligned | The fix to formatting the `--` that weren't aligned was to properly calculate the spacing needed | 
Inputs | get_wild_card_color | test if the method is able to apply validation and prevent unknown options from being selected | The method should prompt the user to re-enter the option if it's invalid | The validation worked and told the user that the selected option doesn't exist, but it didn't allow the user to re-enter the option | I fixed this by running a while loop around the input until the input provided by the user was valid. | 

## Phase 3 + Ensuring Quality through tests and resolving bugs

Phase 3 of development began with the creation of the following modules:

1. Game - The sole purpose of this module was to add a level of abstraction to the code by importing all the dependencies inside it and batching some of the methods into funcitons. This module also controlled various elements of the game such as handling the player turns, checking win conditions, etc.
2. Computer - The purpose of this module was to carry out the main functionalities relating to the computer and it's moves.

The 3rd phase of development was completing by carrying out various tests on the modules and hte Classes held within them. Some of the tests that were carried out have been displayed in the table below:

Module name | Class | Test description | Expected outcome | Actual outcome | How bugs were resolved | 
--- | --- | --- | --- | --- | --- | 
Computer | check_move | Test if the check_move methods returns {"move":"pull_card","card":None} when the computer hand doesn't have any cards that match the top deck card | The method should return {"move":"pull_card","card":None} | The test returned {"move":"pull_card","card":None} | NA | 
Computer | check_move | Test if the check_move methods returns {"move":"use_card","card":matching_card} when the computer hand has a card that matches the top deck card |  The method should return {"move":"pull_card","card":matching card} | The test returned {"move":"pull_card","card":matching card} | NA |
Game | get_turn | Test if the next_turn method updates the player turn to the next player | The next_turn method should update the player turn to the next player | The player turn wasn't updated when the next_turn method was used | This bug was resolved by updating the variable instead of re-assigning it to the same value | 
Game | check_win | Test if the check_win method returns {"game_over":True, "winner":"Computer"} if the computer hand is empty first  | The method should return {"game_over":True, "winner":"Computer"} | The method returned {"game_over":False, "winner":None} | The bug was caused due to an typo made in the if statement that checked the how many cards were left in the computer hand, fixing the typo resolved the bug. | 

# Reflection on key design challenges, innovations and how they were solved
Some of the key design challenges I faced during the creation of the game have been stated below:
1. Handling player turns when a power card such as `reverse` or `skip turn` is played.
2. Handling wild cards and ensuring that they are reset to `BLACK` once they are returned to the deck
3. Managing code complexity and increasing abstraction in the code
4. 





















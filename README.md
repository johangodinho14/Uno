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









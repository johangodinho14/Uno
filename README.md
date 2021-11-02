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
** Potential problems discovered **
1. Due to the scope of the game being massive, my main goal was to make sure that the code was concise and didn't repeat a lot to ensure simplicity.
2. Since the game includes cards, I wanted to make sure that the cards being used in the game could be changed without having to hard code them into the main code.
3. Due to the different moving bits of the game, I wanted to ensure that there isn't one big file that includes most of the code, as it would become difficult to manage the code.

**Potential Solution**
Based on the overall problem (challenege) and the potential problems that I discovered during the early planning phases, some of the solutions I planned have been stated below: 
* Making sure the project follows a modular approach, so that individual elements of the game can be stored in an organised manner in different module files.
* Making sure the proect followed OOP, to ensure the use of abstraction and simplicity in the main code. This would help increase readability and also ensure that the code can be managed easily.
* Making sure that the game is able to read a config file that will include default settings of the game, such as the cards that are to be used in the deck



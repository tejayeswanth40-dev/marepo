# CS108_PROJECT_TOPIC_2 : Mini Game Hub

## Basic Features of the Project :
We are building a secure, multiuser gaming hub that integrates bash scripting for authentication (with the help of main.sh file) and Python(Pygame) 
for the game play ,which are completely based on numpy arrays. 2 Authenticated-players select a game from a menu and play the game by displaying Python 
based GUI(presented with the help of game.py file). The Game Hub of this project includes 3 games tictactoe , othello , connect4 and the basic versions 
of these 3 games are specified in the folder 'games'. The Hub aslo records the data and detailed history of all the authenticated players registered and 
played the above games. 

## Directory Architecture and its Explication :
1. __main.sh__ handles user authentication before launching the game design.
2. __users.tsv__ stores the hashed values of passwords.
3. __game.py__ receives the 2 authenticated usernames and manages the full Python side flow:the game menu, game play and post-game recordings.
4. __history.csv__ contains data of winner, loser, date and game name.
5. __leaderboard.sh__ prints a formatted table to the terminal showing, per game, per user, no.of wins and losses with win/loss ratio.
6. __games/__ is subdirectory that contains the code for the above 3 games which are written and to be implemented in python.

## Work plan and Implementation :
We will start our project by creating a common base __main.sh__ that will be shared across all the games either for authentication or registration. 
And then designing or creating the files suggested in the system architecture of the given project. And then we will first try to make the most basic 
versions of the above 3 games in the subdirectory __games/__ and check the basic code functionalities and proper connections between all the files and 
libraries, including a common class for all the games , a method to call all the games from __game.py__ itself .

Further work includes managing the data and statistics of all the authenticated users who have played the game in the respective history.csv files and final 
post game loop creation. We will try to implement the graphics for each game once we are done with the basic codes. And finally we will finish the 
README and Report to our project. 

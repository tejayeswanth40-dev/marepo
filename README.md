# CS108_PROJECT_TOPIC_2 : Mini Game Hub

## Basic Features of the Project :
We built a secure, multiuser gaming hub that integrates bash scripting for authentication (with the help of main.sh file) and Python(Pygame) 
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
6. __games/__ is subdirectory that contains the code, logics and gamelogos for the above 3 games which are written and to be implemented in python.
7. __base.py__ contains the baseclass for the management of all the games.
8. __show_plots.py__ contains the program for analysing the data in history.csv and plot the bar graphs and pie charts.
9. __report.tex__ has latex code on our insights, explanations and details regarding this project.
10. __Makefile__ has the suitable program to compile the report.tex file into formatted report.pdf.
  
## Libraries required for the game hub
pygame,numpy,matplotlib,os,sys,subprocess,python3

## Starting of engine and playing the games :
Open this repository in your local device and
1. Run the shell command bash main.sh in your terminal.
2. If you are a registered user then enter the password for authentication.
3. If you are not a registered user then register yourselves using the instructions given in the terminal.
4. Once both the users are authenticated and the required libraries are installed in your local device then a home page window with a title "Game Hub" will open      with an enter button.
5. Use the enter button to enter into menu page of the hub.
6. Press the 'x' button to exit the hub.
7. Menu page contains all the three game (tictactoe, othello, connect4) icons and click on the icons to play a graphical induced 2v2 game.
8. If a game ends, then a new winner display window will open showing the winner in this game and certain buttons to view stats. 
9. Now select the respective buttons to view the stats of all the players in each game which will be printed in terminal in the format of a table after sorting. 
10. Then a window showing a bar graph (stats of top 5 winning players) and a pie chart (gameplays of each game) will be shown.
11. Now you can use other buttons named "Return to menu" to return the menu page and "Exit" to quit the game and exit the program.

### To check report.pdf :
- Run "make" inside this repository.
- This will create report.pdf
- To delete all created additional files created during the compilation of report.tex run "make cleantemp"
- To delete all the files includig report.pdf created during the compilation of report.tex run "make clean"
   
### Tic-Tac-Toe Instructions
- The game is played on a 10×10 grid.
- Two players take turns:
- Player 1 → X
- Player 2 → O
- Click or choose a cell to place your mark.
- The first player to align 5 marks (row, column, or diagonal) wins.
- If all cells are filled with no winner → Draw.

### Othello Instructions
- The game is played on an 8×8 board.
- Players take turns placing discs:
- Player 1 → Black
- Player 2 → White
- A move is valid only if it flips at least one opponent disc.
- All opponent discs between your new disc and your existing disc get flipped.
- If a player has no valid moves, the turn is skipped.
- The game ends when no moves are possible for both players.
- Player with the most discs wins.

### Connect4 Instructions
- The game is played on a vertical grid (7 columns × 7 rows).
- Players take turns dropping discs into a column:
- Player 1 → Red
- Player 2 → Yellow
- Discs fall to the lowest empty space in the column.
- First player to connect 4 discs in a row (horizontal, vertical, diagonal) wins.
- If the board fills up with no winner → Draw.

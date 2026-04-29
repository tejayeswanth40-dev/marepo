import numpy as np
import matplotlib.pyplot as plt
import csv
import subprocess
"""
This file reads the history.csv file and plots the stats of the players and games played using matplotlib.
The left plot is a bar graph showing the top 5 players with the most wins and the right plot is a pie chart showing the distribution of games played.

"""

top_players = []
frequencies = []

#Reads history.csv file and extracts the top 5 player's data.
#It also extracts the data on games.

with open('history.csv', 'r') as file:
    reader = csv.reader(file)
    player_wins = {}
    game_counts = {}
    for row in reader:
        winner = row[0]
        if winner in player_wins:
            player_wins[winner] += 1
        else:
            player_wins[winner] = 1

        game = row[3]
        if game in game_counts:
            game_counts[game] += 1
        else:
            game_counts[game] = 1
                
    sorted_players = sorted(player_wins.items(), key=lambda x: x[1], reverse=True)
    top_players = [player[0] for player in sorted_players[:5]]
    frequencies = [player[1] for player in sorted_players[:5]]
    top_players_x = np.array(top_players)
    frequencies_y = np.array(frequencies)
        
    game_labels = list(game_counts.keys())
    game_sizes = list(game_counts.values())
    game_sizes_pie = np.array(game_sizes)

    #This subplot represents bar graph regarding the top 5 players.
    plt.subplot(1, 2, 1)
    plt.bar(top_players_x, frequencies_y, color = 'r', label='Top 5 Players with Most Wins')  
    plt.title("Top 5 Players with Most Wins")
    plt.xlabel("Players")
    plt.ylabel("Number of Wins")
    plt.grid(True, axis='y', linestyle='--', linewidth=0.5)

    #This subplot represents pie chart regarding the games.
    plt.subplot(1, 2, 2)
    plt.pie(game_sizes_pie, labels=game_labels, autopct='%1.1f%%', startangle=140)
    plt.title("Distribution of Games Played")
    plt.show()
    plt.pause(0.1)
        
#!/bin/bash
# Sorting option provided by user (wins, losses, or win/loss_ratio)
sort_by=$1 
if [ "$sort_by" == "wins" ]; then # Sortvalue for wins
    sort_value=3
elif [ "$sort_by" == "losses" ]; then # Sortvalue for losses
    sort_value=4
elif [ "$sort_by" == "win/loss_ratio" ]; then # Sortvalue for win/loss ratio
    sort_value=5
else # Invalid sorting option
    echo "Invalid sorting option. Please choose 'wins', 'losses', or 'win/loss_ratio'."
    exit 1
fi
# This awk command processes history.csv file and calculates wins, losses, and win/loss ratio for each user and game combination.
# win/loss ratio is written upto 2 decimal places.
awk -F "," '
 { user_game_data = $1 "," $4
    wins[user_game_data]++ 
    user_game_data = $2 "," $4
    losses[user_game_data]++ 
    }
    END {
    print "\033[36mGame,Username,Wins,Losses,Win/Loss Ratio\033[0m"
        for (game in wins) {
            split(game, subarray, ",")
                Username=subarray[1]
                Game=subarray[2]
                Wins=wins[game]
                Losses=losses[game] + 0
                if (Losses != 0) {
                winlossRatio=Wins/Losses }
                else {winlossRatio=1000} 
            printf "%s,%s,%d,%d,%.2f\n", Game, Username, Wins, Losses, winlossRatio
        }
        for (game in losses) {
            if (!(game in wins)) { 
                split(game, subarray, ",")
                    Username=subarray[1]
                    Game=subarray[2]
                    Wins=wins[game] + 0
                    Losses=losses[game]
                    winlossRatio=Wins/Losses
                printf "%s,%s,%d,%d,%.2f\n", Game, Username, Wins, Losses, winlossRatio
            }
        }
    }' history.csv > leaderboard.csv
# leaderboard.csv file contains the data without sorting.
# The following command sorts the leaderboard.csv file based on the user's choice and displays it in a formatted table.
(head -n 1 leaderboard.csv && tail -n +2 leaderboard.csv | sort -t "," -k$sort_value,$sort_value -nr) | column -t -s ","
rm leaderboard.csv

#!/bin/bash
sort_by=$1
if [ "$sort_by" == "wins" ]; then
    sort_value=3
elif [ "$sort_by" == "losses" ]; then
    sort_value=4
elif [ "$sort_by" == "win/loss_ratio" ]; then
    sort_value=5
else
    echo "Invalid sorting option. Please choose 'wins', 'losses', or 'win/loss_ratio'."
    exit 1
fi

awk -F "," '
 { user_game_data = $1 "," $4
    wins[user_game_data]++
    user_game_data = $2 "," $4
    losses[user_game_data]++
    }
    END {
    print "\033[36m Game, Username, Wins, Losses, Win/Loss Ratio\033[0m"
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
    }' history.csv | column -t -s "," | sort -t "," -k$sort_value -rn
    

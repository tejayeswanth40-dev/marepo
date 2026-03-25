#!/bin/bash

login1=false
login2=false
while true; do
    read -p "Enter Player 1 username: " usrname1
        if awk -F'\t' '$1 == "'$usrname1'" {exit 0 } END {exit 1}' users.tsv; then
            while true; do
                read -p "Enter Player 1 password: " pass1
                hashpass1=$(echo -n "$pass1" | sha256sum | awk '{print $1}')
                if  awk -F'\t' '$1 == "'$usrname1'" && $2 == "'$hashpass1'" {exit 0 } END {exit 1}' users.tsv; then
                    echo "Player 1 logged in successfully."
                    login1=true
                    #login if usr2 is also matching
                    break
                else
                    echo "Incorrect password for Player 1, please enter password again."
                    continue
                fi
            done
        else
            echo "Username not found for Player 1, Would you like to register or enter username again."
            read -p "Enter 'r' to register or any other character to enter username again: " choice1

            if [ "$choice1" == "r" ]; then
                while true; do
                    # Registration process for Player 1
                    read -p "Enter a new username for Player 1: " usrname1
                    if awk -F'\t' '$1 == "'$usrname1'" {exit 0 } END {exit 1}' users.tsv ; then
                        echo "Username already exists. Please choose a different username."
                        continue
                    else
                        read -p "Enter a new password for Player 1: " pass1
                        hashpass1=$(echo -n "$pass1" | sha256sum | awk '{print $1}')
                        echo -e "$usrname1\t$hashpass1" >> users.tsv
                        echo "Player 1 registered successfully."
                        login1=true
                        break
                    fi
                done
                break # Exit the first loop after successful registration
            elif [ "$choice1" != "r" ]; then
                # Loop back to username input for Player 1
                echo "Fresh Start"
                continue
            fi
        fi
    break # Exit the first loop after successful login
done
while true; do
    read -p "Enter Player 2 username: " usrname2
        if awk -F'\t' '$1 == "'$usrname2'" {exit 0 } END {exit 1}' users.tsv && $usrname2 != $usrname1 ; then
            while true; do
                read -p "Enter Player 2 password: " pass2
                hashpass2=$(echo -n "$pass2" | sha256sum | awk '{print $1}')
                if awk -F'\t' '$1 == "'$usrname2'" && $2 == "'$hashpass2'" {exit 0 } END {exit 1}' users.tsv; then
                    echo "Player 2 logged in successfully."
                    login2=true
                    break
                else
                    echo "Incorrect password for Player 2, please enter password again."
                    continue
                fi
            done
        else
            echo "Username not found for Player 2 or username same as Player 1, Would you like to register or enter username again."
            read -p "Enter 'r' to register or any other character to enter username again: " choice2

            if [ "$choice2" == "r" ]; then
                while true; do
                    # Registration process for Player 2
                    read -p "Enter a new username for Player 2: " usrname2
                    if awk -F'\t' '$1 == "'$usrname2'" {exit 0 } END {exit 1}' users.tsv; then
                        echo "Username already exists. Please choose a different username."
                        continue
                    else
                        read -p "Enter a new password for Player 2: " pass2
                        hashpass2=$(echo -n "$pass2" | sha256sum | awk '{print $1}')
                        echo -e "$usrname2\t$hashpass2" >> users.tsv
                        echo "Player 2 registered successfully."
                        login2=true
                        break
                    fi
                done
                break # Exit the first loop of usrname2 after successful registration
            elif [ "$choice2" != "r" ]; then
                # Loop back to username input for Player 2
                echo "Fresh Start"
                continue
            fi
        fi
    break # Exit the first loop of usrname2 after successful login
done
if [ "$login1" = true ] && [ "$login2" = true ]; then
    echo "Both players logged in successfully. Starting the game..."
    # Call the game script
    python3 game.py "$usrname1" "$usrname2"
else
    echo "Login failed for one or both players. Exiting."
    exit 1
fi
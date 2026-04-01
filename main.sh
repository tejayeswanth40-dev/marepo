#!/bin/bash

# Checks if the username entered is present in users.tsv
scan_users() {
    if grep -qE "^${1}"$'\t' users.tsv; then
        return 0
    else
        return 1
    fi
}
# Checks if the username and password are present in users.tsv
pass_check() {
    if grep -qE "^${1}"$'\t'"${2}$" users.tsv; then
        return 0
    else
        return 1
    fi
}
login1=false
login2=false
while true; do
        # READ USERNAME AND PASSWORD FOR PLAYER 1
    read -p "Enter Player 1 username: " usrname1
        if scan_users "$usrname1"; then
            while true; do
                read -s -p "Enter Player 1 password: " pass1
                echo
                read -s -p "Re-enter Player 1 password: " pass1_confirm
                echo
                if [ "$pass1" != "$pass1_confirm" ]; then
                    echo "Passwords do not match.Please enter the password again."
                    read -p "'x' to terminate the session and any other character to enter password again: " choice4
                    if [ "$choice4" == "x" ]; then
                        exit 1 # Terminate
                    else
                        continue # Enter password for Player 1 again
                    fi
                fi
                hashpass1=$(echo -n "$pass1" | sha256sum | awk '{print $1}')
                if pass_check "$usrname1" "$hashpass1"; then
                    echo "Player 1 logged in successfully."
                    login1=true
                    break # Login successful for player 1
                else
                    echo "Incorrect password for Player 1, please enter the password again."
                    read -p "'x' to terminate the session and any other character to enter password again: " choice0
                    if [ "$choice0" == "x" ]; then
                        exit 1 #Terminate
                    else
                        continue #Enter password for Player 1 again
                    fi
                fi
            done # Login loop for player 1 ENDS
        else
            echo "Username not found for Player 1, Would you like to register or enter username again."
            read -p "Enter 'r' to register and 'x' to terminate session or any other character to enter username again: " choice1
                # REGISTERATION FOR PLAYER 1
            if [ "$choice1" == "r" ]; then
                while true; do
                    read -p "Enter a new username for Player 1: " usrname1
                    if scan_users "$usrname1"; then
                        echo "Username already exists. Please choose a different username."
                        continue
                    else
                        read -s -p "Enter a new password for Player 1: " pass1
                        echo
                        read -s -p "Re-enter the new password for Player 1: " pass1_confirm
                        echo
                        if [ "$pass1" != "$pass1_confirm" ]; then
                            echo "Passwords do not match. Please enter the new password again."
                            read -p "'x' to terminate the session and any other character to enter password again: " choice5
                            if [ "$choice5" == "x" ]; then
                                exit 1 # Terminate
                            else
                                continue # Enter new password for Player 1 again
                            fi
                        fi
                        hashpass1=$(echo -n "$pass1" | sha256sum | awk '{print $1}')
                        echo -e "$usrname1\t$hashpass1" >> users.tsv
                        echo "Player 1 registered successfully."
                        login1=true
                        break # Registered successfully for player 1
                    fi
                done
                break # Exit the first loop after successful registration
            elif [ "$choice1" == "x" ]; then
                exit 1 # Terminate
            else
                echo "Fresh Start"
                continue # Go back to the start, enter username for player 1
            fi
        fi
    break # Exit the first loop after successful login
done
        # READ USERNAME AND PASSWORD FOR PLAYER 2
while true; do
    read -p "Enter Player 2 username: " usrname2
        if scan_users "$usrname2" && [ "$usrname2" != "$usrname1" ]; then
            while true; do
                read -s -p "Enter Player 2 password: " pass2
                echo
                read -s -p "Re-enter Player 2 password: " pass2_confirm
                echo
                if [ "$pass2" != "$pass2_confirm" ]; then
                    echo "Passwords do not match. Please enter the password again."
                    read -p "'x' to terminate the session and any other character to enter password again: " choice6
                    if [ "$choice6" == "x" ]; then
                        exit 1 # Terminate
                    else
                        continue # Enter password for Player 2 again
                    fi
                fi
                hashpass2=$(echo -n "$pass2" | sha256sum | awk '{print $1}')
                if pass_check "$usrname2" "$hashpass2"; then
                    echo "Player 2 logged in successfully."
                    login2=true
                    break # Login successful for player 2
                else
                    echo "Incorrect password for Player 2, please enter password again."
                    read -p "'x' to terminate the session and any other character to enter password again: " choice3
                    if [ "$choice3" == "x" ]; then
                        exit 1 # Terminate
                    else
                        continue # Enter password for Player 2 again
                    fi
                fi
            done
        else
            echo "Username not found for Player 2 or username same as Player 1, Would you like to register or enter username again."
            read -p "Enter 'r' to register and 'x' to terminate the session or any other character to enter username again: " choice2
                    # REGISTERATION FOR PLAYER 2
            if [ "$choice2" == "r" ]; then
                while true; do
                    read -p "Enter a new username for Player 2: " usrname2
                    if scan_users "$usrname2"; then
                        echo "Username already exists. Please choose a different username."
                        continue
                    else
                        read -s -p "Enter a new password for Player 2: " pass2
                        echo
                        read -s -p "Re-enter the new password for Player 2: " pass2_confirm
                        echo
                        if [ "$pass2" != "$pass2_confirm" ]; then
                            echo "Passwords do not match. Please enter the new password again."
                            read -p "'x' to terminate the session and any other character to enter password again: " choice7
                            if [ "$choice7" == "x" ]; then
                                exit 1 # Terminate
                            else
                                continue # Enter new password for Player 2 again
                            fi
                        fi
                        hashpass2=$(echo -n "$pass2" | sha256sum | awk '{print $1}')
                        echo -e "$usrname2\t$hashpass2" >> users.tsv
                        echo "Player 2 registered successfully."
                        login2=true
                        break # Registered successfully for player 2
                    fi
                done
                break # Exit the first loop of usrname2 after successful registration
            elif [ "$choice2" == 'x' ]; then
                exit 1 # Terminate
            else
                echo "Fresh Start"
                continue # Go back to the start, enter username for player 2
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
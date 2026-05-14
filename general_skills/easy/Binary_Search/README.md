# Overview

#### This challenge gives us a shell script implementing a number guessing game and the challenge description already hints that we should use the `Binary Search` algorithm to solve it efficiently. The goal of this challenge is basically to correctly guess a random number between `1` and `1000` within only `10` guesses in order to retrieve the flag.

> *Description of **Binary Search**:*
```
Want to play a game? As you use more of the shell, you might be interested in how they work!
Binary search is a classic algorithm used to quickly find an item in a sorted list.
Can you find the flag? You'll have 1000 possibilities and only 10 guesses.

Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics.
Practicing the fundamentals manually might help you in the future when you have to write your own tools!

You can download the challenge files here:

challenge.zip
ssh -p 53137 ctf-player@atlas.picoctf.net

Using the password 83dcefb7. Accept the fingerprint with yes, and ls once connected to begin.
Remember, in a shell, passwords are hidden!
```

> ***guessing_game.sh** contents:*
```
#!/bin/bash

# Generate a random number between 1 and 1000
target=$(( (RANDOM % 1000) + 1 ))

echo "Welcome to the Binary Search Game!"
echo "I'm thinking of a number between 1 and 1000."

# Trap signals to prevent exiting
trap 'echo "Exiting is not allowed."' INT
trap '' SIGQUIT
trap '' SIGTSTP

# Limit the player to 10 guesses
MAX_GUESSES=10
guess_count=0

while (( guess_count < MAX_GUESSES )); do
    read -p "Enter your guess: " guess

    if ! [[ "$guess" =~ ^[0-9]+$ ]]; then
        echo "Please enter a valid number."
        continue
    fi

    (( guess_count++ ))

    if (( guess < target )); then
        echo "Higher! Try again."
    elif (( guess > target )); then
        echo "Lower! Try again."
    else
        echo "Congratulations! You guessed the correct number: $target"

        # Retrieve the flag from the metadata file
        flag=$(cat /challenge/metadata.json | jq -r '.flag')
        echo "Here's your flag: $flag"
        exit 0  # Exit with success code
    fi
done

# Player has exceeded maximum guesses
echo "Sorry, you've exceeded the maximum number of guesses."
exit 1  # Exit with error code to close the connection
```

# Analysis

#### Looking at the shell script we can see that the program generates a random number between `1` and `1000` and only allows the player to make `10` guesses. In this case the challenge name `Binary Search` hints that we should repeatedly divide the search range in half in order to guarantee finding the correct number within the guess limit.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Binary_Search]
└─# unzip challenge.zip
Archive:  challenge.zip
   creating: home/ctf-player/drop-in/
  inflating: home/ctf-player/drop-in/guessing_game.sh

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Binary_Search]
└─# ls
challenge.zip  home

```

#### The shell script tells us whether the guessed number is higher or lower than the target which is exactly how the `Binary Search` algorithm works. Basically we start in the middle of the range and depending on the output we repeatedly divide the remaining search space in half until we find the correct number.

```
                ...
                (( guess_count++ ))

                if (( guess < target )); then
                    echo "Higher! Try again."
                elif (( guess > target )); then
                    echo "Lower! Try again."
                else
                    echo "Congratulations! You guessed the correct number: $target"

                    # Retrieve the flag from the metadata file
                    flag=$(cat /challenge/metadata.json | jq -r '.flag')
                    echo "Here's your flag: $flag"
                ...
```

# Solution

#### We can simply connect to the remote server through `SSH` and use the `Binary Search` algorithm to narrow down the possible range after every guess. In this case we successfully guessed the correct number within `9` guesses and the server prints the flag.

```
┌──(root💀lsd-AbsentRobust)-[~/…/Binary_Search/home/ctf-player/drop-in]
└─# ssh -p 53137 ctf-player@atlas.picoctf.net
Warning: Permanently added '[atlas.picoctf.net]:53137' (ED25519) to the list of known hosts.
ctf-player@atlas.picoctf.net's password:
Welcome to the Binary Search Game!
I'm thinking of a number between 1 and 1000.
Enter your guess: 500
Lower! Try again.
Enter your guess: 250
Higher! Try again.
Enter your guess: 335
Lower! Try again.
Enter your guess: 292
Lower! Try again.
Enter your guess: 271
Higher! Try again.
Enter your guess: 280
Higher! Try again.
Enter your guess: 285
Lower! Try again.
Enter your guess: 283
Higher! Try again.
Enter your guess: 284
Congratulations! You guessed the correct number: 284
Here's your flag: picoCTF{g00d_gu355_ee8225d0}
Connection to atlas.picoctf.net closed.
```

```
picoCTF{g00d_gu355_ee8225d0}
```

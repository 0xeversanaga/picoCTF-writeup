


Claim offer

picoCTF-writeup-main.zip
Zip Archive
here's the .zip, I just want you to deeply analyze the wordings, typing, grammar structure, the way I write and everything that is written there.

# Overview

#### This challenge gives us a `.zip` file containing a broken Python file and based on the challenge description it hints that one of the commits caused the issue in the program. The goal of this challenge is basically to inspect the Git commit history and identify who made the suspicious commit preventing the program from properly working.

> *Description of **Blame_Game**:*
```
Someone's commits seems to be preventing the program from working. Who is it?
You can download the challenge files here:
challenge.zip
```

> ***message.py** contents:*
```python
print("Hello, World!"
```

# Analysis

#### After extracting the `.zip` file we can see that the directory contains a `.git` repository and a Python file named `message.py`. Looking at the Python file we can immediately notice that the closing parenthesis is missing which means one of the commits probably modified the file incorrectly.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Blame_Game]
└─# unzip challenge.zip
Archive:  challenge.zip
   creating: drop-in/
...

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Blame_Game]
└─# cd drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# ls
message.py
```

#### Since this is a Git challenge we can inspect the commit history using `git log`, but in this case the repository contains thousands of commits which makes manually scrolling very annoying.
```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# git --no-pager log | wc -l # it is so long and git log just gives a pager and it will take a long time to scroll
3011
```

#### Using `tail` allows us to inspect the oldest commits and eventually reveals a suspicious author name containing the flag itself. The commit message `optimize file size of prod code` also matches the broken Python file because the closing parenthesis was probably removed to "reduce" the file size.
```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# git --no-pager log | tail -n 20

    important business work

commit ccf857444761e8380204eafd76e677f9e7e71a94
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    important business work

commit 0fe87f16cbd8129ed5f7cf2f6a06af6688665728
Author: picoCTF{@sk_th3_1nt3rn_ea346835} <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    optimize file size of prod code

commit 7e8a2415b6cca7d0d0002ff0293dd384b5cc900d
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    create top secret project
```

# Solution

#### We can simply inspect the oldest commits using `git log` together with `tail` until we find the suspicious commit author. In this case the flag is directly embedded in the `Author` field of the malicious commit.

```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# git --no-pager log | tail -n 10 | head -n 1
Author: picoCTF{@sk_th3_1nt3rn_ea346835} <ops@picoctf.com>
```

```
picoCTF{@sk_th3_1nt3rn_ea346835}
```

Send me the challenge details first:

challenge name: Binary Search

description:
"Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.

Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

You can download the challenge files here:

challenge.zip
ssh -p 53137 ctf-player@atlas.picoctf.net

Using the password 83dcefb7. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!"

source code or binary behavior:
filename: challenge.zip inside the challenge.zip resides message.py
contents of message.py:
'print("Hello, World!"'

terminal transcript/output:

"""
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Binary_Search]
└─# unzip challenge.zip
Archive:  challenge.zip
   creating: home/ctf-player/drop-in/
  inflating: home/ctf-player/drop-in/guessing_game.sh

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Binary_Search]
└─# ls
challenge.zip  home

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Binary_Search]
└─# cd home

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Binary_Search/home]
└─# ls
ctf-player

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Binary_Search/home]
└─# cd ctf-player

┌──(root💀lsd-AbsentRobust)-[~/…/easy/Binary_Search/home/ctf-player]
└─# ls
drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/easy/Binary_Search/home/ctf-player]
└─# ls -la
drwxr-xr-x root root 38 B Thu May 14 23:10:05 2026 .
drwxr-xr-x root root 38 B Thu May 14 23:10:05 2026 ..
drwxr-xr-x root root 60 B Mon Mar 11 23:51:22 2024 drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/easy/Binary_Search/home/ctf-player]
└─# cd drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/Binary_Search/home/ctf-player/drop-in]
└─# ls
guessing_game.sh

┌──(root💀lsd-AbsentRobust)-[~/…/Binary_Search/home/ctf-player/drop-in]
└─# cat guessing_game.sh

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

┌──(root💀lsd-AbsentRobust)-[~/…/Binary_Search/home/ctf-player/drop-in]
└─# ssh -p 53137 ctf-player@atlas.picoctf.net                                                                                                                                                                  Warning: Permanently added '[atlas.picoctf.net]:53137' (ED25519) to the list of known hosts.
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
"""
exploit steps or vulnerability: checking the long commit logs
final flag: picoCTF{g00d_gu355_ee8225d0}

# Overview

#### This challenge gives us a shell script implementing a number guessing game and the challenge description already hints that we should use the `Binary Search` algorithm to solve it efficiently. The goal of this challenge is basically to correctly guess a random number between `1` and `1000` within only `10` guesses in order to retrieve the flag.

> *Description of **Binary Search**:*
```
Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses.

Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools!

You can download the challenge files here:

challenge.zip
ssh -p 53137 ctf-player@atlas.picoctf.net

Using the password 83dcefb7. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!
```

> ***guessing_game.sh** contents:*
```bash
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

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Binary_Search]
└─# cd home

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Binary_Search/home]
└─# ls
ctf-player

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Binary_Search/home]
└─# cd ctf-player

┌──(root💀lsd-AbsentRobust)-[~/…/easy/Binary_Search/home/ctf-player]
└─# ls
drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/easy/Binary_Search/home/ctf-player]
└─# ls -la
drwxr-xr-x root root 38 B Thu May 14 23:10:05 2026 .
drwxr-xr-x root root 38 B Thu May 14 23:10:05 2026 ..
drwxr-xr-x root root 60 B Mon Mar 11 23:51:22 2024 drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/easy/Binary_Search/home/ctf-player]
└─# cd drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/Binary_Search/home/ctf-player/drop-in]
└─# ls
guessing_game.sh
```

#### The shell script tells us whether the guessed number is higher or lower than the target which is exactly how the `Binary Search` algorithm works. Basically we start in the middle of the range and depending on the output we repeatedly divide the remaining search space in half until we find the correct number.

```
┌──(root💀lsd-AbsentRobust)-[~/…/Binary_Search/home/ctf-player/drop-in]
└─# cat guessing_game.sh

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

Send me the challenge details first:

challenge name: Binary Search

description:
"""
Do you know how to move between directories and read files in the shell? Start the container, ssh to it, and then ls once connected to begin.

Login via ssh as ctf-player with the password, 8c606eb1 on the host wily-courier.picoctf.net and port 58423.
"""

source code or binary behavior: None
filename: None
contents: None

terminal transcript/output:

"""
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# ssh ctf-player@wily-courier.picoctf.net -p 57182
Warning: Permanently added '[wily-courier.picoctf.net]:57182' (ED25519) to the list of known hosts.
ctf-player@wily-courier.picoctf.net's password:
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 6.17.0-1013-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_
ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly /
ctf-player@pico-chall$ cd /
ctf-player@pico-chall$ ls
2of3.flag.txt  boot       dev  home                      lib    media  opt   root  sbin  sys  usr
bin            challenge  etc  instructions-to-3of3.txt  lib64  mnt    proc  run   srv   tmp  var
ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_//4t3r_
ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly ~
ctf-player@pico-chall$ cd ~
ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in
ctf-player@pico-chall$ cat 3of3.flag.txt
0b24fc4f}ctf-player@pico-chall$ ls drop-in/
1of3.flag.txt  instructions-to-2of3.txt
ctf-player@pico-chall$
"""
exploit steps or vulnerability: Basic linux path traversal and file read
final flag: picoCTF{run_s4n1ty_run}

# Overview

#### This challenge gives us access to a remote Linux machine through `SSH` and tests basic shell navigation knowledge such as changing directories and reading files. The goal of this challenge is basically to follow the instructions hidden in different directories and combine all the flag fragments together to reveal the complete flag.

> *Description of **Binary Search**:*
```
Do you know how to move between directories and read files in the shell? Start the container, ssh to it, and then ls once connected to begin.

Login via ssh as ctf-player with the password, 8c606eb1 on the host wily-courier.picoctf.net and port 58423.
```

# Analysis

#### After connecting to the remote server through `SSH` we can list the files in the current directory using `ls` and immediately notice a file named `1of3.flag.txt` together with another instruction file. Reading the first flag file reveals only a partial flag which means we need to continue following the instructions to retrieve the remaining parts.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# ssh ctf-player@wily-courier.picoctf.net -p 57182
Warning: Permanently added '[wily-courier.picoctf.net]:57182' (ED25519) to the list of known hosts.
ctf-player@wily-courier.picoctf.net's password:
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 6.17.0-1013-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage
This system has been minimized by removing packages and content that are
not required on a system that users do not log into.

To restore this content, you can run the 'unminimize' command.

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

ctf-player@pico-chall$ ls
1of3.flag.txt  instructions-to-2of3.txt

ctf-player@pico-chall$ cat 1of3.flag.txt
picoCTF{xxsh_

ctf-player@pico-chall$ cat instructions-to-2of3.txt
Next, go to the root of all things, more succinctly `/`
```

#### The instructions tells us to go to the root directory `/` where another flag fragment and another instruction file exists. In Linux the root directory is basically the top-level directory containing all other system directories.

```
ctf-player@pico-chall$ cd /

ctf-player@pico-chall$ ls
2of3.flag.txt  boot       dev  home                      lib    media  opt   root  sbin  sys  usr
bin            challenge  etc  instructions-to-3of3.txt  lib64  mnt    proc  run   srv   tmp  var

ctf-player@pico-chall$ cat 2of3.flag.txt
0ut_0f_//4t3r_

ctf-player@pico-chall$ cat instructions-to-3of3.txt
Lastly, ctf-player, go home... more succinctly `~`
```

#### The final instructions tells us to go back to the home directory using `~` and this reveals the final part of the flag. Combining all three fragments together gives us the completed flag.

```
ctf-player@pico-chall$ cd ~

ctf-player@pico-chall$ ls
3of3.flag.txt  drop-in

ctf-player@pico-chall$ cat 3of3.flag.txt
0b24fc4f}

ctf-player@pico-chall$ ls drop-in/
1of3.flag.txt  instructions-to-2of3.txt
```

# Solution

#### We can simply follow the instructions provided in every text file and navigate through the filesystem using basic Linux commands such as `cd`, `ls`, and `cat`. After collecting all three flag fragments and combining them together we get the complete flag.

```
picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
```

Send me the challenge details first:

challenge name: Nice netcat

description:
"""
There is a nice program that you can talk to by using this command in a shell:

$ nc wily-courier.picoctf.net 49657, but it doesn't speak English...
"""

source code or binary behavior: None
filename: None
contents: None

terminal transcript/output:

"""
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
100
57
52
55
54
125
10

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657 | base64 -w 0 | python -c "print(input())"
MTEyIAoxMDUgCjk5IAoxMTEgCjY3IAo4NCAKNzAgCjEyMyAKMTAzIAo0OCAKNDggCjEwMCAKOTUgCjEwNyAKNDkgCjExNiAKMTE2IAoxMjEgCjMzIAo5NSAKMTEwIAo0OSAKOTkgCjUxIAo5NSAKMTA3IAo0OSAKMTE2IAoxMTYgCjEyMSAKMzMgCjk1IAoxMDAgCjU3IAo1MiAKNTUgCjU0IAoxMjUgCjEwIAo=

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657 | base64 -w 0
MTEyIAoxMDUgCjk5IAoxMTEgCjY3IAo4NCAKNzAgCjEyMyAKMTAzIAo0OCAKNDggCjEwMCAKOTUgCjEwNyAKNDkgCjExNiAKMTE2IAoxMjEgCjMzIAo5NSAKMTEwIAo0OSAKOTkgCjUxIAo5NSAKMTA3IAo0OSAKMTE2IAoxMTYgCjEyMSAKMzMgCjk1IAoxMDAgCjU3IAo1MiAKNTUgCjU0IAoxMjUgCjEwIAo=                                                                                                          
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657 | base64 -w 0 | python -c "print(input())"
MTEyIAoxMDUgCjk5IAoxMTEgCjY3IAo4NCAKNzAgCjEyMyAKMTAzIAo0OCAKNDggCjEwMCAKOTUgCjEwNyAKNDkgCjExNiAKMTE2IAoxMjEgCjMzIAo5NSAKMTEwIAo0OSAKOTkgCjUxIAo5NSAKMTA3IAo0OSAKMTE2IAoxMTYgCjEyMSAKMzMgCjk1IAoxMDAgCjU3IAo1MiAKNTUgCjU0IAoxMjUgCjEwIAo=

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657 | base64 -w 0 | python -c "from base64 import b64decode;print(b64decode(input().encode()).decode().split())"
['112', '105', '99', '111', '67', '84', '70', '123', '103', '48', '48', '100', '95', '107', '49', '116', '116', '121', '33', '95', '110', '49', '99', '51', '95', '107', '49', '116', '116', '121', '33', '95', '100', '57', '52', '55', '54', '125', '10']

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# python3
Python 3.13.3 (main, Apr 10 2025, 21:38:51) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = ['112', '105', '99', '111', '67', '84', '70', '123', '103', '48', '48', '100', '95', '107', '49', '116', '116', '121', '33', '95', '110', '49', '99', '51', '95'\
, '107', '49', '116', '116', '121', '33', '95', '100', '57', '52', '55', '54', '125', '10']
>>> p = ""
>>> for i in a:
...     p += chr(int(i))
...
>>> p
'picoCTF{g00d_k1tty!_n1c3_k1tty!_d9476}\n'
>>>
"""
exploit steps or vulnerability: ASCII encoding and using netcat to connect and get the encoded data
final flag: picoCTF{g00d_k1tty!_n1c3_k1tty!_d9476}

# Overview

#### This challenge gives us a remote service accessible through `netcat` and based on the challenge description it hints that the server output is not written in normal English text. The goal of this challenge is basically to identify what encoding or representation was used by the server and decode it to reveal the actual flag.

> *Description of **Nice netcat**:*
```
There is a nice program that you can talk to by using this command in a shell:

$ nc wily-courier.picoctf.net 49657, but it doesn't speak English...
```

# Analysis

#### Connecting to the remote service using `netcat` reveals a list of numbers printed line by line instead of readable text. In this case the values looks like decimal integers which hints that they are probably ASCII character codes.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657
112
105
99
111
67
84
70
123
103
48
48
100
95
107
49
116
116
121
33
95
110
49
99
51
95
107
49
116
116
121
33
95
100
57
52
55
54
125
10
```

#### To make the output easier to work with we can encode the entire output into a single line using `base64` and then decode it back inside Python to split the values into a proper list.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657 | base64 -w 0
MTEyIAoxMDUgCjk5IAoxMTEgCjY3IAo4NCAKNzAgCjEyMyAKMTAzIAo0OCAKNDggCjEwMCAKOTUgCjEwNyAKNDkgCjExNiAKMTE2IAoxMjEgCjMzIAo5NSAKMTEwIAo0OSAKOTkgCjUxIAo5NSAKMTA3IAo0OSAKMTE2IAoxMTYgCjEyMSAKMzMgCjk1IAoxMDAgCjU3IAo1MiAKNTUgCjU0IAoxMjUgCjEwIAo=

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# nc wily-courier.picoctf.net 49657 | base64 -w 0 | python -c "from base64 import b64decode;print(b64decode(input().encode()).decode().split())"
['112', '105', '99', '111', '67', '84', '70', '123', '103', '48', '48', '100', '95', '107', '49', '116', '116', '121', '33', '95', '110', '49', '99', '51', '95', '107', '49', '116', '116', '121', '33', '95', '100', '57', '52', '55', '54', '125', '10']
```

#### Since the values are ASCII codes we can simply loop through every integer, convert them into characters using Python's `chr()` function, and concatenate them together to reveal the plaintext flag.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Nice_netcat]
└─# python3
Python 3.13.3 (main, Apr 10 2025, 21:38:51) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = ['112', '105', '99', '111', '67', '84', '70', '123', '103', '48', '48', '100', '95', '107', '49', '116', '116', '121', '33', '95', '110', '49', '99', '51', '95', '107', '49', '116', '116', '121', '33', '95', '100', '57', '52', '55', '54', '125', '10']
>>> p = ""
>>> for i in a:
...     p += chr(int(i))
...
>>> p
'picoCTF{g00d_k1tty!_n1c3_k1tty!_d9476}\n'
>>>
```

# Solution

#### We can simply connect to the remote service using `netcat`, identify that the numbers are ASCII decimal values, and convert every integer into its corresponding character. After concatenating all the decoded characters together we reveal the complete flag.

```
picoCTF{g00d_k1tty!_n1c3_k1tty!_d9476}
```


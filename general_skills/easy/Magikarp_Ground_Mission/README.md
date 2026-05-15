# Overview

#### This challenge gives us access to a remote Linux machine through `SSH` and tests basic shell navigation knowledge such as changing directories and reading files. The goal of this challenge is basically to follow the instructions hidden in different directories and combine all the flag fragments together to reveal the complete flag.

> *Description of **Magikarp Ground Mission**:*
```
Do you know how to move between directories and read files in the shell?
Start the container, ssh to it, and then ls once connected to begin.

Login via ssh as ctf-player with the password, 8c606eb1 on the host wily-courier.picoctf.net and port 58423.
```

# Analysis

#### After connecting to the remote server through `SSH` we can list the files in the current directory using `ls` and immediately notice a file named `1of3.flag.txt` together with another instruction file. Reading the first flag file reveals only a partial flag which means we need to continue following the instructions to retrieve the remaining parts.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# ssh ctf-player@wily-courier.picoctf.net -p 58423
Warning: Permanently added '[wily-courier.picoctf.net]:58423' (ED25519) to the list of known hosts.
ctf-player@wily-courier.picoctf.net's password:
Welcome to Ubuntu 18.04.6 LTS (GNU/Linux 6.17.0-1013-aws x86_64)
...

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

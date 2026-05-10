# Overview

#### The last challenge to finish `Python in CTF's` learning path! `what's a net cat?` introduces us to the swiff army knife of networking, famously known as `netcat` or `nc` command. [Netcat](https://en.wikipedia.org/wiki/Netcat) `(nc)` is a networking utility that can create TCP/UDP connections to send, receive, or interact with data across a network.

> *Description:* Using netcat (nc) is going to be pretty important. Can you connect to fickle-tempest.picoctf.net at port 58699 to get the flag?

#### To connect to a server in `netcat`, it follows this format: `netcat <HOST> <PORT>`. It says that after we connect to the provide `server IP` and port we can get the flag!
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/whats_a_net_cat]
└─# nc fickle-tempest.picoctf.net 58699
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_575F8fFd}
```

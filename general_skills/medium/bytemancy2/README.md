# Overview

#### Continuing the `Bytemancy Series`, we are now tackling `bytemancy 2`. I've notice now that it uses `sys` library to get the raw stdin and stripping the new line. This is abit of a challenge but understanding the core concept will make things easier.

> *Description of **bytemancy 2**:*

```
Can you conjure the right bytes? The program's source code can be downloaded here.

Connect to the program with netcat:
$ nc lonely-island.picoctf.net 58148
```

> *app.py with **line numbers**:*
```
01| import sys
02| 
03| while(True):
04|   try:
05|     print('⊹──────[ BYTEMANCY-2 ]──────⊹')
06|     print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
07|     print()
08|     print('Send me the HEX BYTE 0xFF 3 times, side-by-side, no space.')
09|     print()
10|     print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
11|     print('⊹─────────────⟡─────────────⊹')
12|     print('==> ', end='', flush=True)
13|     user_input = sys.stdin.buffer.readline().rstrip(b"\n")
14|     if user_input == b"\xff\xff\xff":
15|       print(open("./flag.txt", "r").read())
16|       break
17|     else:
18|       print("That wasn't it. I got: " + str(user_input))
19|       print()
20|       print()
21|       print()
22|   except Exception as e:
23|     print(e)
24|     break
```

# Analysis

#### To get the flag we must enter the right bytes which are these raw `\xff\xff\xff`, which cannot be typed traditionally. This forces us to innovate and find another way to send these bytes to get the flag.

```
13|     user_input = sys.stdin.buffer.readline().rstrip(b"\n")
14|     if user_input == b"\xff\xff\xff":
15|       print(open("./flag.txt", "r").read())
```

> *Attempting to print using `echo`:*

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/bytemancy2]
└─# echo -en "\xff\xff\xff" | xxd
00000000: ffff ff                                  ...
```

#### It seems that we cannot achieve this with `echo`, because it immidiately sends all the bytes even if the program is still printing the banner. That means we need to use `pwntool`, to send the bytes after receiving `==> ` from standard output.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/bytemancy2]
└─# echo -en "\xff\xff\xff" | nc lonely-island.picoctf.net 58148
⊹──────[ BYTEMANCY-2 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me the HEX BYTE 0xFF 3 times, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> 
```

# Solution

#### Using this `Python` script we can create the connection by calling `start()` and calling `sendlineafter()` to send the correct bytes at the right time.

```
#!/usr/bin/env python3
from pwn import *

HOST = "lonely-island.picoctf.net"
PORT = 54905

def start():
    return remote(HOST, PORT)

def main():
    p = start()

    p.sendlineafter(b"==> ", b"\xff\xff\xff")

    p.interactive()

if __name__ == "__main__":
    main()
```

#### Running it gives us the flag!

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/bytemancy2]
└─# python3 exploit.py
[+] Opening connection to lonely-island.picoctf.net on port 58148: Done
[*] Switching to interactive mode
picoCTF{3ff5_4_d4yz_f0542086}
[*] Got EOF while reading in interactive
$
```
```
picoCTF{3ff5_4_d4yz_f0542086}
```

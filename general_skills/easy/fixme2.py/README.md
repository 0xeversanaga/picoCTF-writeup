# Overview

#### Moving on to `fixme2.py`, categorized as `easy` this is going to be simple. It just gave us basically `fixme1.py` but with an *if-else condition* to check if `flag` is empty.

> *fixme2.py with **line numbers**:*
```
01| import random
02|
03|
04|
05| def str_xor(secret, key):
06|     #extend key to secret length
07|     new_key = key
08|     i = 0
09|     while len(new_key) < len(secret):
10|         new_key = new_key + key[i]
11|         i = (i + 1) % len(key)
12|     return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
13|
14|
15| flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x18) + chr(0x11) + chr(0x41) + chr(0x09) + chr(0x5f) + chr(0x1f) + chr(0x10) + chr(0x3b) + chr(0x1b) + chr(0x55) + chr(0x1a) + chr(0x34) + chr(0x5d) + chr(0x51) + chr(0x40) + chr(0x54) + chr(0x09) + chr(0x05) + chr(0x04) + chr(0x57) + chr(0x1b) + chr(0x11) + chr(0x31) + chr(0x5f) + chr(0x51) + chr(0x52) + chr(0x46) + chr(0x00) + chr(0x5f) + chr(0x5a) + chr(0x0b) + chr(0x19)
16|
17|
18| flag = str_xor(flag_enc, 'enkidu')
19|
20| # Check that flag is not empty
21| if flag = "":
22|   print('String XOR encountered a problem, quitting.')
23| else:
24|   print('That is correct! Here\'s your flag: ' + flag)
```

# Analysis

#### Running it now gives us a different error. `SyntaxError` seems to be at the start of the `if` statement. We need to fix this error by changing how the `flag` is compared. `flag = ""` assigns `flag` to be `""` and it should be `if flag == ""`.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/fixme2.py]
└─# python3 fixme2.py
  File "/sec/root/picoCTF-writeup/general_skills/easy/fixme2.py/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

# Solution

#### 

```
import random

def str_xor(secret, key):
    #extend key to secret length
    new_key = key
    i = 0
    while len(new_key) < len(secret):
        new_key = new_key + key[i]
        i = (i + 1) % len(key)
    return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x58) + chr(0x18) + chr(0x11) + chr(0x41) + chr(0x09) + chr(0x5f) + chr(0x1f) + chr(0x10) + chr(0x3b) + chr(0x1b) + chr(0x55) + chr(0x1a) + chr(0x34) + chr(0x5d) + chr(0x51) + chr(0x40) + chr(0x54) + chr(0x09) + chr(0x05) + chr(0x04) + chr(0x57) + chr(0x1b) + chr(0x11) + chr(0x31) + chr(0x5f) + chr(0x51) + chr(0x52) + chr(0x46) + chr(0x00) + chr(0x5f) + chr(0x5a) + chr(0x0b) + chr(0x19)

flag = str_xor(flag_enc, 'enkidu')

# Check that flag is not empty
if flag == "":
  print('String XOR encountered a problem, quitting.')
else:
  print('That is correct! Here\'s your flag: ' + flag)
```

#### And got the flag!

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/fixme2.py]
└─# python3 fixme2.py
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}

```

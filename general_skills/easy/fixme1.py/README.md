# Overview

#### We're now tackling the `Python in CTF's` learning path! And also `PicoCTF` changed their brand into `CyLab Security Academy`.

___

<div style="text-align: center;">
	<img src="https://i.imgur.com/rBpE8l1.png">
</div>

___

#### In the `Problem set 1`, there's `fixme1.py` and `fixme2.py`. We will solve the first one. The code seems okay and seems to need some *fixing*.

> *fixme1.py with **line numbers**:*
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
15| flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x5e) + chr(0x52) + chr(0x0c) + chr(0x01) + chr(0x42) + chr(0x57) + chr(0x59) + chr(0x0a) + chr(0x14)
16|
17|
18| flag = str_xor(flag_enc, 'enkidu')
19|   print('That is correct! Here\'s your flag: ' + flag)
```

# Analysis

#### Running it gives us an `IndentationError`, so we just need fix it and along with it remove some unnecessary new lines. 

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/fixme1.py]
└─# python3 fixme1.py
  File "/sec/root/picoCTF-writeup/general_skills/easy/fixme1.py/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
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

flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5a) + chr(0x07) + chr(0x00) + chr(0x46) + chr(0x0b) + chr(0x1a) + chr(0x5a) + chr(0x1d) + chr(0x1d) + chr(0x2a) + chr(0x06) + chr(0x1c) + chr(0x5a) + chr(0x5c) + chr(0x55) + chr(0x40) + chr(0x3a) + chr(0x5e) + chr(0x52) + chr(0x0c) + chr(0x01) + chr(0x42) + chr(0x57) + chr(0x59) + chr(0x0a) + chr(0x14)

flag = str_xor(flag_enc, 'enkidu')
print('That is correct! Here\'s your flag: ' + flag)
```

#### And got the flag!

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/fixme1.py]
└─# python3 fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}

```

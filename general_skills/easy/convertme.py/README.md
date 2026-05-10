# Overview

#### Now it's `convertme.py`, introduces us to different number systems. Converting from `base-10` or decimal base to `base-2` or binary base.

> *convertme.py with **line numbers**:*
```
01| import random
02|
03| def str_xor(secret, key):
04|     #extend key to secret length
05|     new_key = key
06|     i = 0
07|     while len(new_key) < len(secret):
08|         new_key = new_key + key[i]
09|         i = (i + 1) % len(key)
10|     return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
11|
12| flag_enc = chr(0x15) + chr(0x07) + chr(0x08) + chr(0x06) + chr(0x27) + chr(0x21) + chr(0x23) + chr(0x15) + chr(0x5f) + chr(0x05) + chr(0x08) + chr(0x2a) + chr(0x1c) + chr(0x5e) + chr(0x1e) + chr(0x1b) + chr(0x3b) + chr(0x17) + chr(0x51) + chr(0x5b) + chr(0x58) + chr(0x5c) + chr(0x3b) + chr(0x42) + chr(0x57) + chr(0x5c) + chr(0x0d) + chr(0x5f) + chr(0x06) + chr(0x46) + chr(0x5c) + chr(0x13)
13|
14| num = random.choice(range(10,101))
15|
16| print('If ' + str(num) + ' is in decimal base, what is it in binary base?')
17|
18| ans = input('Answer: ')
19|
20| try:
21|   ans_num = int(ans, base=2)
22|
23|   if ans_num == num:
24|     flag = str_xor(flag_enc, 'enkidu')
25|     print('That is correct! Here\'s your flag: ' + flag)
26|   else:
27|     print(str(ans_num) + ' and ' + str(num) + ' are not equal.')
28|
29| except ValueError:
30|   print('That isn\'t a binary number. Binary numbers contain only 1\'s and 0\'s')
```

# Solution

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/convertme.py]
└─# python3 convertme.py
If 65 is in decimal base, what is it in binary base?
Answer: 1000001
That is correct! Here's your flag: picoCTF{4ll_y0ur_b4535_722f6b39}
```

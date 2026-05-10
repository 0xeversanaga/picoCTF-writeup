# Overview

#### We are now on `Problem set 2`, and there's `PW Crack 1` and `PW Crack 2`. We will solve the first one. The code seems okay and seems to need some fixing.

> *level1.py with **line numbers**:*
```
01| ### THIS FUNCTION WILL NOT HELP YOU FIND THE FLAG --LT ########################
02| def str_xor(secret, key):
03|     #extend key to secret length
04|     new_key = key
05|     i = 0
06|     while len(new_key) < len(secret):
07|         new_key = new_key + key[i]
08|         i = (i + 1) % len(key)
09|     return "".join([chr(ord(secret_c) ^ ord(new_key_c)) for (secret_c,new_key_c) in zip(secret,new_key)])
10| ###############################################################################
11|
12|
13| flag_enc = open('level1.flag.txt.enc', 'rb').read()
14|
15|
16|
17| def level_1_pw_check():
18|     user_pw = input("Please enter correct password for flag: ")
19|     if( user_pw == "691d"):
20|         print("Welcome back... your flag, user:")
21|         decryption = str_xor(flag_enc.decode(), user_pw)
22|         print(decryption)
23|         return
24|     print("That password is incorrect")
25|
26|
27|
28| level_1_pw_check()
```

# Analysis

#### This one's easy as a cake, it asks us for a password. But if we closely examine `level_1_pw_check()` the password is inside the *if statement*.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/PW_Crack_1]
└─# python3 level1.py
Please enter correct password for flag: test123
That password is incorrect
```

# Solution

#### Present at `line 19` the password is `691d`. We can get the flag by entering the password.

```
17| def level_1_pw_check():
18|     user_pw = input("Please enter correct password for flag: ")
19|     if( user_pw == "691d"):
20|         print("Welcome back... your flag, user:")
21|     ...
```

#### And got the flag!

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/PW_Crack_1]
└─# python3 level1.py
Please enter correct password for flag: 691d
Welcome back... your flag, user:
picoCTF{545h_r1ng1ng_56891419}
```

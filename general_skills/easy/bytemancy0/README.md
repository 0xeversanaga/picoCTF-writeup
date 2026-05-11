# Overview

#### We're now going to solve the `Bytemancy Series`. Starting from `bytemancy 0`, it seems that we need to provide the right combination of bytes to get the flag.

> *Description of **bytemancy 0**:*

```
Can you conjure the right bytes? The program's source code can be downloaded here.

Connect to the program with netcat:
$ nc candy-mountain.picoctf.net 56583
```

> *app.py with **line numbers**:*
```
01| while(True):
02|   try:
03|     print('⊹──────[ BYTEMANCY-0 ]──────⊹')
04|     print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
05|     print()
06|     print('Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.')
07|     print()
08|     print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
09|     print('⊹─────────────⟡─────────────⊹')
10|     user_input = input('==> ')
11|     if user_input == "\x65\x65\x65":
12|       print(open("./flag.txt", "r").read())
13|       break
14|     else:
15|       print("That wasn't it. I got: " + str(user_input))
16|       print()
17|       print()
18|       print()
19|   except Exception as e:
20|     print(e)
21|     break
```

# Analysis

#### Checking the `line 11` we can observe this if-statement where we can achieve the flag. We need `user_input` to be `"\x65\x65\x65"` and its just basically `'eee'`.

```
10|     user_input = input('==> ')
11|     if user_input == "\x65\x65\x65":
12|       print(open("./flag.txt", "r").read())
13|       break
```

# Solution

#### Connecting to the server and after entering the right bytes we should get the flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/bytemancy0]
└─# nc candy-mountain.picoctf.net 56583
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> eee
picoCTF{pr1n74813_ch4r5_2f7a75e5}
```

#### Here goes the flag!

```
picoCTF{pr1n74813_ch4r5_2f7a75e5}
```

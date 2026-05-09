# Overview

#### Now it's `vault-door-4`, it uses ASCII encoding for the flag. This is pretty simple, we just need to decode `myBytes` to get the flag.

> *Source code with **line numbers**:*
```
01| import java.util.*;
02|
03| class VaultDoor4 {
04|     public static void main(String args[]) {
05|       ...
15|     }
16|
17|     // I made myself dizzy converting all of these numbers into different bases,
18|     // so I just *know* that this vault will be impenetrable. This will make Dr.
19|     // Evil like me better than all of the other minions--especially Minion
20|     // #5620--I just know it!
21|     //
22|     //  .:::.   .:::.
23|     // :::::::.:::::::
24|     // :::::::::::::::
25|     // ':::::::::::::'
26|     //   ':::::::::'
27|     //     ':::::'
28|     //       ':'
29|     // -Minion #7781
30|     public boolean checkPassword(String password) {
31|         byte[] passBytes = password.getBytes();
32|         byte[] myBytes = {
33|             106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
34|             0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
35|             0142, 0131, 0164, 063 , 0163, 0137, 066 , 064 ,
36|             'e' , '1' , '3' , 'd' , '0' , '0' , 'b' , '2' ,
37|         };
38|         for (int i=0; i<32; i++) {
39|             if (passBytes[i] != myBytes[i]) {
40|                 return false;
41|             }
42|         }
43|         return true;
44|     }
45| }
```

# Analysis

#### Interesting, `myBytes` is composed of numbers represented in different [number system](https://en.wikipedia.org/wiki/Numeral_system). We can see it uses `base-10`, `base-16`, and `base-8`. Now that we know how the flag is *'protected'*, we can now easily decode them and get the flag!

```
31|         byte[] passBytes = password.getBytes();
32|         byte[] myBytes = {
33|             106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
34|             0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
35|             0142, 0131, 0164, 063 , 0163, 0137, 066 , 064 ,
36|             'e' , '1' , '3' , 'd' , '0' , '0' , 'b' , '2' ,
37|         };
```

# Solution

#### This `Python` script goes through every item in the array and uses `chr()` to decode and append the character to make up the flag.

```
def getFlag(enc: list) -> str:
    flag_part = ""

    for i in enc:
        if type(i) == str:
            flag_part += i

        else:
            flag_part += chr(i)

    return "picoCTF{" + flag_part + "}"

encoded = [106, 85, 53, 116, 95, 52, 95, 98,
           0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30,
           0x66, 0x5f, 0o142, 0o131, 0o164, 0o63,
           0o163, 0o137, 0o66, 0o64, 'e', '1', '3',
           'd', '0', '0', 'b', '2']

flag = getFlag(encoded)

print(flag)
```

#### And got the flag!

```
picoCTF{jU5t_4_bUnCh_0f_bYt3s_64e13d00b2}
```

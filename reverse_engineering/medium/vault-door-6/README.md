# Overview

#### Ohh, this is getting interesting now. *Mr. Minion* is trying [XOR operation](https://en.wikipedia.org/wiki/XOR_cipher) to protect the flag. Unfortunately it is badly designed and can easily be decoded.

> *Source code with **line numbers**:*
```
01| import java.util.*;
02|
03| class VaultDoor6 {
04|     public static void main(String args[]) {
05|      ...
15|     }
16|
17|     // Dr. Evil gave me a book called Applied Cryptography by Bruce Schneier,
18|     // and I learned this really cool encryption system. This will be the
19|     // strongest vault door in Dr. Evil's entire evil volcano compound for sure!
20|     // Well, I didn't exactly read the *whole* book, but I'm sure there's
21|     // nothing important in the last 750 pages.
22|     //
23|     // -Minion #3091
24|     public boolean checkPassword(String password) {
25|         if (password.length() != 32) {
26|             return false;
27|         }
28|         byte[] passBytes = password.getBytes();
29|         byte[] myBytes = {
30|             0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
31|             0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
32|             0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
33|             0xa , 0x67, 0x65, 0x67, 0x62, 0x6c, 0x6d, 0x66,
34|         };
35|         for (int i=0; i<32; i++) {
36|             if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
37|                 return false;
38|             }
39|         }
40|         return true;
41|     }
42| }
```

# Analysis

#### In `line 36` we can see it uses `^` on `passBytes` and then subtracting it to `myBytes[i]` to check if the character is correct. `passBytes` is XORed by `0x55` and this is our key to solving this vault. We just need to do the same operation to every byte in the `myBytes` array and get the flag!

```
29|         byte[] myBytes = {
30|          ...
34|         };
35|         for (int i=0; i<32; i++) {
36|             if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
37|                 return false;
38|             }
39|         }
```

# Solution

#### With this `Python` script we can get the flag. It just loops through the list, XORing the value and appending the ASCII character that makes up the flag.

```
import base64

def getFlag(enc: list) -> str:
    flag_part = ""

    for i in enc:
        flag_part += chr(i ^ 0x55)

    return "picoCTF{" + flag_part + "}"

encoded = [0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
           0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
           0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
           0xa , 0x67, 0x65, 0x67, 0x62, 0x6c, 0x6d, 0x66]

flag = getFlag(encoded)

print(flag)
```

#### And got the flag!

```
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_2027983}
```

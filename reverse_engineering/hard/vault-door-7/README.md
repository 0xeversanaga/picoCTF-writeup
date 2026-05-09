# Overview

#### We're now on `vault-door-7`, nearing the end we've finally entered the `hard` category. In this challenge, the main focus seems to be about [bit shifting](https://en.wikipedia.org/wiki/Bitwise_operation\#Bit_shifts) and this way if packing a `byte` into a single `integer`. This is quite tough and requires understanding about bitwise operations.

> *Source code with **line numbers**:*
```
01| import java.util.*;
02| ...
06| class VaultDoor7 {
07|     public static void main(String args[]) {
08|      ...
18|     }
19|
20|     // Each character can be represented as a byte value using its
21|     // ASCII encoding. Each byte contains 8 bits, and an int contains
22|     // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
23|     // example: if the hex string is "01ab", then those can be
24|     // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
25|     // bytes are represented as binary, they are:
26|     //
27|     // 0x30: 00110000
28|     // 0x31: 00110001
29|     // 0x61: 01100001
30|     // 0x62: 01100010
31|     //
32|     // If we put those 4 binary numbers end to end, we end up with 32
33|     // bits that can be interpreted as an int.
34|     //
35|     // 00110000001100010110000101100010 -> 808542562
36|     //
37|     // Since 4 chars can be represented as 1 int, the 32 character password can
38|     // be represented as an array of 8 ints.
39|     //
40|     // - Minion #7816
41|     public int[] passwordToIntArray(String hex) {
42|         int[] x = new int[8];
43|         byte[] hexBytes = hex.getBytes();
44|         for (int i=0; i<8; i++) {
45|             x[i] = hexBytes[i*4]   << 24
46|                  | hexBytes[i*4+1] << 16
47|                  | hexBytes[i*4+2] << 8
48|                  | hexBytes[i*4+3];
49|         }
50|         return x;
51|     }
52|
53|     public boolean checkPassword(String password) {
54|         if (password.length() != 32) {
55|             return false;
56|         }
57|         int[] x = passwordToIntArray(password);
58|         return x[0] == 1096770097
59|             && x[1] == 1952395366
60|             && x[2] == 1600270708
61|             && x[3] == 1601398833
62|             && x[4] == 1716808014
63|             && x[5] == 1734293606
64|             && x[6] == 909455713
65|             && x[7] == 1664103218;
66|     }
67| }
```

# Analysis

#### The `passwordToIntArray()` divides the `32 byte` flag into 8 integers. The main concept is that each byte contains 8 bits, and an int contains 32 bits, so it's possible to pack `4 bytes` into a single `integer`. Let's take a closer look at what's happening.

```
41|     public int[] passwordToIntArray(String hex) {
42|         int[] x = new int[8];
43|         byte[] hexBytes = hex.getBytes();
44|         for (int i=0; i<8; i++) {
45|             x[i] = hexBytes[i*4]   << 24
46|                  | hexBytes[i*4+1] << 16
47|                  | hexBytes[i*4+2] << 8
48|                  | hexBytes[i*4+3];
49|         }
50|         return x;
51|     }
```

> *Behind the scenes: **test.py***
```
from sys import argv

if __name__ == '__main__':
    if len(argv) != 2:
        print(f"{argv[0]} <data>")
        exit()
    ...
    for o in range(0, 8):
        f1 = l[o*4] << 24 # first character
        f2 = l[o*4+1] << 16
        f3 = l[o*4+2] << 8
        f4 = l[o*4+3]

        t[o] = f1 | f2 | f3 | f4
        print(f"{data[o*4]}: {f1} -- {bin(ord(data[o*4]))} -> {bin(f1)}")
        print(f"{data[o*4+1]}: {f2} -- {bin(ord(data[o*4+1]))} ->{bin(f2)}")
        print(f"{data[o*4+2]}: {f3} -- {bin(ord(data[o*4+2]))} ->{bin(f3)}")
        print(f"{data[o*4+3]}: {f4} -- {bin(ord(data[o*4+3]))} ->{bin(f4)}")
        print(f"total: {t[o]} -- {bin(t[o])}\n")

    print(t)
```
> *Output:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/reverse_engineering/hard/vault-door-7]
└─# python3 test.py picoctf_test_script_0xeversanaga
p: 1879048192 -- 0b1110000 -> 0b1110000000000000000000000000000
i: 6881280 -- 0b1101001 ->0b11010010000000000000000
c: 25344 -- 0b1100011 ->0b110001100000000
o: 111 -- 0b1101111 ->0b1101111
total: 1885954927 -- 0b1110000011010010110001101101111
...
```

#### We just need to extract the `4 bytes` inside the `integers` to get the flag.

```
encoded = [ 1096770097, 1952395366, 1600270708, 1601398833,
            1716808014, 1734293606, 909455713, 1664103218, ]
```

# Solution

#### This `Python` script reverses the bit shift operations and appends the extracted characters that will allow us to retrieve the flag.

```
def getFlag(enc: list) -> str:
    flag_part = ""

    for num in enc:
        flag_part += chr(num >> 24)
        flag_part += chr((num >> 16) & 0b11111111)
        flag_part += chr((num >> 8) & 0b11111111)
        flag_part += chr(num & 0b11111111)

    return "picoCTF{" + flag_part + "}"

encoded = [ 1096770097, 1952395366, 1600270708, 1601398833,
            1716808014, 1734293606, 909455713, 1664103218, ]

flag = getFlag(encoded)

print(flag)
```

#### And got the flag!

```
picoCTF{A_b1t_0f_b1t_sh1fTiNg_8f651ac032}
```

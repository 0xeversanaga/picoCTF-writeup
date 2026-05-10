# Overview

#### Finally, this is the last vault and we will have finished the `Vault Door Series`. This one's kinda hard to read so let's beautify it using https://codebeautify.org/javaviewer. There is certainly alot going on here, given that it is on `hard` category. It seems this is all about `bit manipulation` working with `bitwise operations` to scramble all the `32 bytes` of the flag.

> *Source code with **line numbers**:*
```
01| // These pesky special agents keep reverse engineering our source code and then
02| // breaking into our secret vaults. THIS will teach those sneaky sneaks a
03| // lesson.
04| //
05| // -Minion #0891
06| import java.util.*;
07| import javax.crypto.Cipher;
08| import javax.crypto.spec.SecretKeySpec;
09| import java.security.*;
10| class VaultDoor8 {
11|   public static void main(String args[]) {
12|    ...
22|   }
23|   public char[] scramble(String password) {
24|     /* Scramble a password by transposing pairs of bits. */
25|     char[] a = password.toCharArray();
26|     for (int b = 0; b < a.length; b++) {
27|       char c = a[b];
28|       c = switchBits(c, 1, 2);
29|       c = switchBits(c, 0, 3); /* c = switchBits(c, 14, 3); c = switchBits(c, 2, 0); */
30|       c = switchBits(c, 5, 6);
31|       c = switchBits(c, 4, 7);
32|       c = switchBits(c, 0, 1); /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */
33|       c = switchBits(c, 3, 4);
34|       c = switchBits(c, 2, 5);
35|       c = switchBits(c, 6, 7);
36|       a[b] = c;
37|     }
38|     return a;
39|   }
40|   public char switchBits(char c, int p1, int p2) {
41|     /* Move the bit in position p1 to position p2, and move the bit
42|     that was in position p2 to position p1. Precondition: p1 < p2 */
43|     char mask1 = (char)(1 << p1);
44|     char mask2 = (char)(1 << p2); /* char mask3 = (char)(1 << p1 << p2); mask1++; mask1--; */
45|     char bit1 = (char)(c & mask1);
46|     char bit2 = (char)(c & mask2);
47|     /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
48|        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
49|     char rest = (char)(c & ~(mask1 | mask2));
50|     char shift = (char)(p2 - p1);
51|     char result = (char)((bit1 << shift) | (bit2 >> shift) | rest);
52|     return result;
53|   }
54|   public boolean checkPassword(String password) {
55|     char[] scrambled = scramble(password);
56|     char[] expected = {
57|       0xF4, 0xC0, 0x97, 0xF0,
58|       0x77, 0x97, 0xC0, 0xE4,
59|       0xF0, 0x77, 0xA4, 0xD0,
60|       0xC5, 0x77, 0xF4, 0x86,
61|       0xD0, 0xA5, 0x45, 0x96,
62|       0x27, 0xB5, 0x77, 0xA4,
63|       0xA4, 0xA4, 0xD1, 0xE1,
64|       0xC2, 0xB4, 0xA4, 0xF1
65|     };
66|     return Arrays.equals(scrambled, expected);
67|   }
68| }
```

# Analysis

#### This vault is centered scrambling the bits using `scramble()` and we need to reverse each operation done to all the bits. It's noticeable that `scramble()` uses alot of `switchBits()` to do all the *'scrambling'*. We're gonna recreate the same function into `Python` to make this alot easier. After we successfully recreate `switchBits` into Python, getting the flag will be easy!

```
40|   public char switchBits(char c, int p1, int p2) {
41|     /* Move the bit in position p1 to position p2, and move the bit
42|     that was in position p2 to position p1. Precondition: p1 < p2 */
43|     char mask1 = (char)(1 << p1);
44|     char mask2 = (char)(1 << p2); /* char mask3 = (char)(1 << p1 << p2); mask1++; mask1--; */
45|     char bit1 = (char)(c & mask1);
46|     char bit2 = (char)(c & mask2);
47|     /* System.out.println("bit1 " + Integer.toBinaryString(bit1));
48|        System.out.println("bit2 " + Integer.toBinaryString(bit2)); */
49|     char rest = (char)(c & ~(mask1 | mask2));
50|     char shift = (char)(p2 - p1);
51|     char result = (char)((bit1 << shift) | (bit2 >> shift) | rest);
52|     return result;
53|   }
```

# Solution

#### This is `switchBits()` in `Python`, all we need to do now is reverse the switching done in `scramble()` and then finally get the flag!.

```
def switchBits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2

    bit1 = c & mask1
    bit2 = c & mask2

    rest = c & ~(mask1 | mask2)

    shift = p2 - p1

    result = ((bit1 << shift) |
              (bit2 >> shift) |
              rest)

    return result
```

> *This is the `unscram()` that takes an integer and reverses all the **bit switching**, and it returns a `str`*.

```
def unscram(c):
    c = switchBits(c, 6, 7);
    c = switchBits(c, 2, 5);
    c = switchBits(c, 3, 4);
    c = switchBits(c, 0, 1);
    c = switchBits(c, 4, 7);
    c = switchBits(c, 5, 6);
    c = switchBits(c, 0, 3);
    c = switchBits(c, 1, 2);

    return chr(c)
```

#### Now that we've defined `unscram()` we can finally get the flag using everything we've gathered.

```
def switchBits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2

    bit1 = c & mask1
    bit2 = c & mask2

    rest = c & ~(mask1 | mask2)

    shift = p2 - p1

    result = ((bit1 << shift) |
              (bit2 >> shift) |
              rest)

    return result

def unscram(c):
    c = switchBits(c, 6, 7);
    c = switchBits(c, 2, 5);
    c = switchBits(c, 3, 4);
    c = switchBits(c, 0, 1);
    c = switchBits(c, 4, 7);
    c = switchBits(c, 5, 6);
    c = switchBits(c, 0, 3);
    c = switchBits(c, 1, 2);

    return chr(c)

def getFlag(enc: list) -> str:
    flag_part = ""

    for num in enc:
        flag_part += unscram(num)

    return "picoCTF{" + flag_part + "}"

encoded = [ 0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4,
            0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86,
            0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xA4,
            0xA4, 0xA4, 0xD1, 0xE1, 0xC2, 0xB4, 0xA4, 0xF1 ]

flag = getFlag(encoded)

print(flag)
```

#### And got the flag!

```
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_bbb568cb7}
```

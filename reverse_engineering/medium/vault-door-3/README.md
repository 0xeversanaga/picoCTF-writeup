# Overview

#### I think the author forgot that there exist number after `1`, but let's proceed with `vault-door-3`. I uses for-loops and byte arrays to scramble the flag.

> *Source code with **line numbers**:*
```
01| import java.util.*;
02|
03| class VaultDoor3 {
04|     public static void main(String args[]) {
05|         VaultDoor3 vaultDoor = new VaultDoor3();
06|         Scanner scanner = new Scanner(System.in);
07|         System.out.print("Enter vault password: ");
08|         String userInput = scanner.next();
09|         String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
10|         if (vaultDoor.checkPassword(input)) {
11|             System.out.println("Access granted.");
12|         } else {
13|             System.out.println("Access denied!");
14|         }
15|     }
16|
17|     // Our security monitoring team has noticed some intrusions on some of the
18|     // less secure doors. Dr. Evil has asked me specifically to build a stronger
19|     // vault door to protect his Doomsday plans. I just *know* this door will
20|     // keep all of those nosy agents out of our business. Mwa ha!
21|     //
22|     // -Minion #2671
23|     public boolean checkPassword(String password) {
24|         if (password.length() != 32) {
25|             return false;
26|         }
27|         char[] buffer = new char[32];
28|         int i;
29|         for (i=0; i<8; i++) {
30|             buffer[i] = password.charAt(i);
31|         }
32|         for (; i<16; i++) {
33|             buffer[i] = password.charAt(23-i);
34|         }
35|         for (; i<32; i+=2) {
36|             buffer[i] = password.charAt(46-i);
37|         }
38|         for (i=31; i>=17; i-=2) {
39|             buffer[i] = password.charAt(i);
40|         }
41|         String s = new String(buffer);
42|         return s.equals("jU5t_a_sna_3lpm15g64e_u_4_m1r74d");
43|     }
44| }
```

# Analysis

#### Again the flag is automatically gonna be `32 bytes`. We just need to reverse the operation done with the flag. It seems to be that it uses for-loops to reverse the middle `16 bytes`.

```
27|         char[] buffer = new char[32];
28|         int i;
29|         for (i=0; i<8; i++) {
30|             buffer[i] = password.charAt(i);
31|         }
32|         for (; i<16; i++) {
33|             buffer[i] = password.charAt(23-i);
34|         }
35|         for (; i<32; i+=2) {
36|             buffer[i] = password.charAt(46-i);
37|         }
38|         for (i=31; i>=17; i-=2) {
39|             buffer[i] = password.charAt(i);
40|         }
```

# Solution

#### We are going to translate it to `Python` and get the flag.

```
def getFlag(enc: str) -> str:
    buffer = ('a ' * 32).split() # list with 32 a's

    for i in range(0, 8):
        buffer[i] = enc[i]

    for i in range(8, 16):
        buffer[i] = enc[23 - i]

    for i in range(16, 32, 2):
        buffer[i] = enc[46 - i]

    for i in range(31, 16, -2):
        buffer[i] = enc[i]

    flag_part = "".join(buffer)

    return "picoCTF{"+flag_part+"}"

scrambled = "jU5t_a_sna_3lpm15g64e_u_4_m1r74d"

flag = getFlag(scrambled)

print(flag)
```

#### And got the flag!

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e1675d}
```

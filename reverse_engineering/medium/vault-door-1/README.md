# Overview

#### Next one `vault-door-1`, *Mr. Minion 8728* hopes his `checkPassword()` is UNHACKABLE. Clearly it's not, though his method on obscuring the flag seems messy. We can easily decode it and recover the flag.

> *Source code with **line numbers**:*
```
01| import java.util.*;
02| 
03| class VaultDoor1 {
04|     public static void main(String args[]) {
05|         VaultDoor1 vaultDoor = new VaultDoor1();
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
17|     // I came up with a more secure way to check the password without putting
18|     // the password itself in the source code. I think this is going to be
19|     // UNHACKABLE!! I hope Dr. Evil agrees...
20|     //
21|     // -Minion #8728
22|     public boolean checkPassword(String password) {
23|         return password.length() == 32 &&
24|                password.charAt(0)  == 'd' &&
25|                password.charAt(29) == '4' &&
26|                password.charAt(4)  == 'r' &&
27|                password.charAt(2)  == '5' &&
28|                password.charAt(23) == 'r' &&
29|                password.charAt(3)  == 'c' &&
30|                password.charAt(17) == '4' &&
31|                password.charAt(1)  == '3' &&
32|                password.charAt(7)  == 'b' &&
33|                password.charAt(10) == '_' &&
34|                password.charAt(5)  == '4' &&
35|                password.charAt(9)  == '3' &&
36|                password.charAt(11) == 't' &&
37|                password.charAt(15) == 'c' &&
38|                password.charAt(8)  == 'l' &&
39|                password.charAt(12) == 'H' &&
40|                password.charAt(20) == 'c' &&
41|                password.charAt(14) == '_' &&
42|                password.charAt(6)  == 'm' &&
43|                password.charAt(24) == '5' &&
44|                password.charAt(18) == 'r' &&
45|                password.charAt(13) == '3' &&
46|                password.charAt(19) == '4' &&
47|                password.charAt(21) == 'T' &&
48|                password.charAt(16) == 'H' &&
49|                password.charAt(27) == '0' &&
50|                password.charAt(30) == 'e' &&
51|                password.charAt(25) == '_' &&
52|                password.charAt(22) == '3' &&
53|                password.charAt(28) == 'e' &&
54|                password.charAt(26) == 'a' &&
55|                password.charAt(31) == 'b';
56|     }
57| }
```

# Analysis

#### The `checkPassword()` already gives us the length of the flag which is `32 chars`. We just have to follow the indexes in every `charAt()` and what character does it check to get the `flag`.

```
22|     public boolean checkPassword(String password) {
23|         return password.length() == 32 &&
24|                password.charAt(0)  == 'd' &&
```

# Solution

#### It took maybe 3 minutes and after unscrambling everything I'm left with this.

```
password.charAt(0)  == 'd'
password.charAt(1)  == '3'
password.charAt(2)  == '5'
password.charAt(3)  == 'c'
password.charAt(4)  == 'r'
password.charAt(5)  == '4'
password.charAt(6)  == 'm'
password.charAt(7)  == 'b'
password.charAt(8)  == 'l'
password.charAt(9)  == '3'
password.charAt(10) == '_'
password.charAt(11) == 't'
password.charAt(12) == 'H'
password.charAt(13) == '3'
password.charAt(14) == '_'
password.charAt(15) == 'c'
password.charAt(16) == 'H'
password.charAt(17) == '4'
password.charAt(18) == 'r'
password.charAt(19) == '4'
password.charAt(20) == 'c'
password.charAt(21) == 'T'
password.charAt(22) == '3'
password.charAt(23) == 'r'
password.charAt(24) == '5'
password.charAt(25) == '_'
password.charAt(26) == 'a'
password.charAt(27) == '0'
password.charAt(28) == 'e'
password.charAt(29) == '4'
password.charAt(30) == 'e'
password.charAt(31) == 'b'
```

#### And got the flag!

```
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_a0e4eb}
```

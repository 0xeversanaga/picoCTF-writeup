# Overview

#### We're now going to tackle the vault door series, starting with `vault-door-training`.

> *Source code with **line numbers**:*
```
01| import java.util.*;
02|
03| class VaultDoorTraining {
04|     public static void main(String args[]) {
05|         VaultDoorTraining vaultDoor = new VaultDoorTraining();
06|         Scanner scanner = new Scanner(System.in);
07|         System.out.print("Enter vault password: ");
08|         String userInput = scanner.next();
09|         String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
10|         if (vaultDoor.checkPassword(input)) {
11|             System.out.println("Access granted.");
12|         } else {
13|             System.out.println("Access denied!");
14|         }
15|    }
16|
17|     // The password is below. Is it safe to put the password in the source code?
18|     // What if somebody stole our source code? Then they would know what our
19|     // password is. Hmm... I will think of some ways to improve the security
20|     // on the other doors.
21|     //
22|     // -Minion #9567
23|     public boolean checkPassword(String password) {
24|         return password.equals("w4rm1ng_Up_w1tH_jAv4_0009yrGMeEp");
25|     }
26| }
```

# Solution

#### This one's pretty simple, to gain access inside the vault. The flag is present at the `checkPassword()`.

```
picoCTF{w4rm1ng_Up_w1tH_jAv4_0009yrGMeEp}
```

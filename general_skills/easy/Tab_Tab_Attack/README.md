# Overview

#### This challenge gives us a `.zip` file containing a deeply nested directory structure with very long directory names which makes manually typing the path very annoying. The goal of this challenge is basically to navigate through the nested directories and execute or inspect the final file while using shell tab completion to make navigation easier.

> *Description of **Tab, Tab, Attack**:*
```
Using tabcomplete in the Terminal will add years to your life,
esp. when dealing with long rambling directory structures and filenames.

Addadshashanammu.zip
```

# Analysis

#### After extracting the `.zip` file we can immediately notice that the challenge intentionally creates a very long nested directory structure. In this case manually typing the entire path would be very inconvenient which is why the challenge hints at using terminal tab completion.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Tab_Tab_Attack]
└─# unzip Addadshashanammu.zip
Archive:  Addadshashanammu.zip
   creating: Addadshashanammu/
   creating: Addadshashanammu/Almurbalarammi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/
   creating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/
 extracting: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet.c
  inflating: Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

#### Looking at the extracted files we can see that the final file is an executable binary named `fang-of-haynekhtnamet`. Executing the binary directly reveals the flag immediately.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Tab_Tab_Attack]
└─# ./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

#### The challenge also includes the source code file which confirms that the binary simply prints the flag using `printf()`. Basically the challenge is more focused on shell navigation and tab completion rather than exploitation or reverse engineering.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Tab_Tab_Attack]
└─# cat Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet.c
#include <stdio.h>


int main(){
printf("*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}\n");
}
```

# Solution

#### We can simply use shell tab completion to quickly navigate through the deeply nested directory structure and execute the final binary using `./`. Running the executable prints the flag directly to the terminal.

```
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

```
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

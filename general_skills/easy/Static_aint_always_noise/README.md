# Overview

#### This challenge gives us a binary file together with a helper bash script named `ltdis.sh` which is intended to disassemble the binary and extract useful strings from it. The goal of this challenge is basically to inspect the contents of the binary and identify where the hidden flag exists using either disassembly tools or direct string searching.

> *Description of **Static aint always noise**:*
```
Can you look at the data in this binary? The bash script might help!

static, ltdis.sh
```

> ***ltdis.sh** contents:*
```bash
#!/bin/bash

echo "Attempting disassembly of $1 ..."

#This usage of "objdump" disassembles all (-D) of the first file given by
#invoker, but only prints out the ".text" section (-j .text) (only section
#that matters in almost any compiled program...

objdump -Dj .text $1 > $1.ltdis.x86_64.txt

#Check that $1.ltdis.x86_64.txt is non-empty
#Continue if it is, otherwise print error and eject

if [ -s "$1.ltdis.x86_64.txt" ]
then
        echo "Disassembly successful! Available at: $1.ltdis.x86_64.txt"

        echo "Ripping strings from binary with file offsets..."
        strings -a -t x $1 > $1.ltdis.strings.txt
        echo "Any strings found in $1 have been written to $1.ltdis.strings.txt with file offset"

else
        echo "Disassembly failed!"
        echo "Usage: ltdis.sh <program-file>"
        echo "Bye!"
fi
```

# Analysis

#### Looking at the binary using the `file` command shows that it is an ELF 64-bit executable and it is also not stripped which means symbols and useful strings may still exist inside the binary. In this case the challenge hints that inspecting the binary contents is enough to recover the flag without needing exploitation.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Static_aint_always_noise]
└─# file static
static: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9a00d4dca6b92d22aa0cd1fceffa4ed7495b8534, for GNU/Linux 3.2.0, not stripped
```

#### The provided `ltdis.sh` script uses both `objdump` and `strings` to disassemble the binary and extract readable strings from it. Running the script against the binary generates two output files containing the disassembly and all extracted strings.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Static_aint_always_noise]
└─# bash ltdis.sh static
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

#### Looking through the extracted strings immediately reveals the picoCTF flag stored directly inside the binary data. Basically the binary was not obfuscated at all and the flag can be recovered just by searching readable strings.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Static_aint_always_noise]
└─# cat static.ltdis.strings.txt
    318 /lib64/ld-linux-x86-64.so.2
    471 libc.so.6
    47b puts
    480 __cxa_finalize
    48f __libc_start_main
    4a1 GLIBC_2.2.5
    4ad _ITM_deregisterTMCloneTable
    4c9 __gmon_start__
    4d8 _ITM_registerTMCloneTable
   110b u+UH
   11ca []A\A]A^A_
   2008 Oh hai! Wait what? A flag? Yes, it's around here somewhere!
   20d7 :*3$"
   3020 picoCTF{d15a5m_t34s3r_20335e41}
   3040 GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.0
...
```

#### Even though the challenge provides the helper script we can actually recover the flag much faster using `grep -a` directly on the binary since the flag exists as plaintext inside the executable. The `-a` option forces `grep` to treat the binary as text data and search through it normally.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Static_aint_always_noise]
└─# grep -a "picoCTF" static
�
 �?��  ������o���o���o����o�=@picoCTF{d15a5m_t34s3r_20335e41}GCC: (Ubuntu 9.4.0-1ubuntu1~20.04.2) 9.4.08X|���
```

# Solution

#### We can simply search the binary directly for the `picoCTF{` pattern using `grep -a` since the flag exists in plaintext inside the executable. Even though the provided `ltdis.sh` script works, directly grepping the binary is much faster and immediately reveals the flag.

```
picoCTF{d15a5m_t34s3r_20335e41}
```

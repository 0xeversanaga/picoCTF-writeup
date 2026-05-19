# Overview

#### This challenge gives us a binary file named `strings`, the goal of this challenge is to introduce us the basics of analyzing a binary file.

> *Description of **strings it**:*
```
Can you find the flag in file without running it?
```

# Analysis

#### The file `strings` is a 64-bit ELF program, and running it hints us into the `strings` command.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/strings_it]
└─# file strings
strings: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a0867a67d407f6d2dad90aefc25fd5c89888e12e, for GNU/Linux 3.2.0, not stripped

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/strings_it]
└─# ./strings
Maybe try the 'strings' function? Take a look at the man page
```

#### The description of `strings` from the manual shows that it prints the sequences of printable characters in files.

# Solution

#### Running the `strings` command on the given binary should give us the flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/strings_it]
└─# strings strings | grep pico
picoCTF{5tRIng5_1T_60eA8fdA}
```
```
picoCTF{5tRIng5_1T_60eA8fdA}
```

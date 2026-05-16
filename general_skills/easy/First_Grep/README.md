# Overview

#### This challenge gives us a file containing a huge amount of random looking data and based on the challenge description it hints that manually searching through the file would be very tedious. The goal of this challenge is basically to use command line tools such as `grep` to efficiently search for the flag pattern hidden somewhere inside the file.

> *Description of **First Grep**:*
```
Can you find the flag in the file? This would be really tedious to look through manually,
something tells me there is a better way.

The flag is in this file.
```

# Analysis

#### Looking at the contents of the file we can immediately notice that it mostly contains random nonsense characters and manually inspecting everything would take a very long time. In this case using a pattern searching utility like `grep` is much more efficient since picoCTF flags always follows the format `picoCTF{...}`.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/First_Grep]
└─# cat file
4RD?;7*FK4</!`Z8xM^2em|~1s8]ddQ,]nzW_MNW1lC|ZWhWxWLZEQ^/7
...
```

#### Using `grep` with the string `picoCTF{` successfully reveals the line containing the flag, but it also includes additional nonsense characters because the line contains more data besides the flag itself.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/First_Grep]
└─# grep "picoCTF{" file
4RD?;7*FK4</!`Z8xM^2em|~1s8]ddQ,]nzW_MNW1lC|ZWhWxWLZEQ^/7       Jnd1.<D4BO-=WP7i/2@:?bb0j
```

#### To extract only the flag we can use the `-o` option together with a regular expression that matches the entire picoCTF flag format. Basically the regex searches for `picoCTF{` followed by every character until the closing `}`.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/First_Grep]
└─# grep -o 'picoCTF{[^}]*}' file
picoCTF{grep_is_good_to_find_things_9C6Ef2F7}
```

# Solution

#### We can simply use `grep` together with a regular expression to search for and extract only the picoCTF flag format from the file. Using the `-o` option prints only the matched portion which cleanly reveals the flag without the surrounding nonsense data.

```
picoCTF{grep_is_good_to_find_things_9C6Ef2F7}
```

# Overview

#### This challenge gives us a `.zip` file containing a broken Python file and based on the challenge description it hints that one of the commits caused the issue in the program. The goal of this challenge is basically to inspect the Git commit history and identify who made the suspicious commit preventing the program from properly working.

> *Description of **Blame Game**:*
```
Someone's commits seems to be preventing the program from working. Who is it?
You can download the challenge files here:
challenge.zip
```

> ***message.py** contents:*
```python
print("Hello, World!"
```

# Analysis

#### After extracting the `.zip` file we can see that the directory contains a `.git` repository and a Python file named `message.py`. Looking at the Python file we can immediately notice that the closing parenthesis is missing which means one of the commits probably modified the file incorrectly.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Blame_Game]
└─# unzip challenge.zip
Archive:  challenge.zip
   creating: drop-in/
...

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Blame_Game]
└─# cd drop-in

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# ls
message.py
```

#### Since this is a Git challenge we can inspect the commit history using `git log`, but in this case the repository contains thousands of commits which makes manually scrolling very annoying.
```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# git --no-pager log | wc -l # it is so long and git log just gives a pager and it will take a long time to scroll
3011
```

#### Using `tail` allows us to inspect the oldest commits and eventually reveals a suspicious author name containing the flag itself. The commit message `optimize file size of prod code` also matches the broken Python file because the closing parenthesis was probably removed to "reduce" the file size.
```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# git --no-pager log | tail -n 20

    important business work

commit ccf857444761e8380204eafd76e677f9e7e71a94
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    important business work

commit 0fe87f16cbd8129ed5f7cf2f6a06af6688665728
Author: picoCTF{@sk_th3_1nt3rn_ea346835} <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    optimize file size of prod code

commit 7e8a2415b6cca7d0d0002ff0293dd384b5cc900d
Author: picoCTF <ops@picoctf.com>
Date:   Sat Mar 9 21:09:25 2024 +0000

    create top secret project
```

# Solution

#### We can simply inspect the oldest commits using `git log` together with `tail` until we find the suspicious commit author. In this case the flag is directly embedded in the `Author` field of the malicious commit.

```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Blame_Game/drop-in]
└─# git --no-pager log | tail -n 10 | head -n 1
Author: picoCTF{@sk_th3_1nt3rn_ea346835} <ops@picoctf.com>
```

```
picoCTF{@sk_th3_1nt3rn_ea346835}
```

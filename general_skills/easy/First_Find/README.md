# Overview

#### This challenge gives us a `.zip` archive containing a huge amount of directories and files with the goal of locating a specific file named `uber-secret.txt`. The goal of this challenge is basically to identify where the target file exists inside the extracted directory structure and read its contents to retrieve the flag.

> *Description of **First Find**:*
```
Unzip this archive and find the file named 'uber-secret.txt'
Download zip file
```

# Analysis

#### After extracting the `.zip` archive we can immediately notice that it contains many nested directories and files which would normally make manually searching very tedious. In this case however the output of `unzip` already reveals the exact location of the target file during extraction.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/First_Find]
└─# unzip files.zip
Archive:  files.zip
   creating: files/
   creating: files/satisfactory_books/
   creating: files/satisfactory_books/more_books/
  inflating: files/satisfactory_books/more_books/37121.txt.utf-8
  inflating: files/satisfactory_books/23765.txt.utf-8
  inflating: files/satisfactory_books/16021.txt.utf-8
  inflating: files/13771.txt.utf-8
   creating: files/adequate_books/
   creating: files/adequate_books/more_books/
   creating: files/adequate_books/more_books/.secret/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/
   creating: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/
 extracting: files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
  inflating: files/adequate_books/more_books/1023.txt.utf-8
  inflating: files/adequate_books/46804-0.txt
  inflating: files/adequate_books/44578.txt.utf-8
   creating: files/acceptable_books/
   creating: files/acceptable_books/more_books/
  inflating: files/acceptable_books/more_books/40723.txt.utf-8
  inflating: files/acceptable_books/17880.txt.utf-8
  inflating: files/acceptable_books/17879.txt.utf-8
  inflating: files/14789.txt.utf-8
```

#### Looking closely at the extraction output we can see that `uber-secret.txt` was extracted inside a hidden `.secret` directory nested several levels deep. We can simply use `cat` on the revealed path to read the file contents and retrieve the flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/First_Find]
└─# cat files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt
picoCTF{f1nd_15_f457_ab443fd1}
```

# Solution

#### We can simply inspect the output of the `unzip` command to identify where `uber-secret.txt` was extracted and then read the file using `cat`. The contents of the file directly reveals the flag.

```
picoCTF{f1nd_15_f457_ab443fd1}
```

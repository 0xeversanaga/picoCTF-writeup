# Overview

#### This challenge gives us a very large `.zip` archive containing thousands of directories and files which makes manually inspecting every file unrealistic. The goal of this challenge is basically to use Linux command line utilities to recursively search through all the extracted files and locate the hidden picoCTF flag.

> *Description of **Big Zip**:*
```
Unzip this archive and find the flag.
Download zip file
```

# Analysis

#### After extracting the archive we can immediately notice that the extracted directory contains a massive amount of nested folders and text files. In this case manually opening files one by one would take an extremely long time which is why recursive search commands become very useful.

```
 extracting: big-zip-files/folder_wdhgdgrbfc/izpsdjrflyxcpuhjtaflbtp.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/fxaxiryjldhjugrsxhndjglp.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_qmzrrkkuaqnol.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/xktktzhdxnfu.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/puqtvrnhomqbrkguy.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_czpkyijqgdzhwkfkyd.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/ncpphsegf.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/rpagkqbzcuxepx.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/pdppdhedydlawgvhwym.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/qbwalzyyprvrcjpepe.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_ljeldszgyuc.txt
 extracting: big-zip-files/folder_wdhgdgrbfc/lmjsuinfffmpmyjmmk.txt
 extracting: big-zip-files/folder_wdhgdgrbfc/tdwocpenvymtoj.txt
 extracting: big-zip-files/folder_wdhgdgrbfc/fdsjfllubxcxwhpv.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_jyvxtmmtpl.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_epcuiockebhmxxtago.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/tvnwbgmapeulf.txt
 extracting: big-zip-files/folder_wdhgdgrbfc/finitvya.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/bondkyoxvdcgxyq.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_hacfyxtdwkdiycfwatiyvusg.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_jdlhinpycace.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/gnsnwwhmlslslscapr.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/file_ximyquuowm.txt
  inflating: big-zip-files/folder_wdhgdgrbfc/siizcxeduftjnvian.txt
  inflating: big-zip-files/mktyhgmedcj.txt
```

#### Looking at the extracted contents we can confirm that there are too many files to inspect manually. We can first try locating a file directly named `flag.txt` using `find`, but the command does not return anything which means the flag is probably hidden somewhere inside a random file.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Big_Zip]
└─# ls -la
drwxr-xr-x root root  92 B  Sat May 16 17:02:01 2026 .
drwxr-xr-x root root 4.0 KB Sat May 16 17:00:25 2026 ..
drwxrwxr-x root root  48 KB Sun May  3 22:12:06 2020 big-zip-files
.rw-r--r-- root root 3.0 MB Fri Aug  4 22:06:41 2023 big-zip-files.zip

┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/Big_Zip]
└─# cd big-zip-files

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Big_Zip/big-zip-files]
└─# find . -name flag.txt
```

#### Since picoCTF flags always follows the `picoCTF{}` format we can recursively search through every file using `grep -r` to locate the exact line containing the flag. This immediately reveals both the file path and the hidden flag.

```
┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Big_Zip/big-zip-files]
└─# grep -r . "picoCTF"
grep: picoCTF: No such file or directory

┌──(root💀lsd-AbsentRobust)-[~/…/general_skills/easy/Big_Zip/big-zip-files]
└─# grep -r "picoCTF{" .
./folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:information on the record will last a billion years. Genes and brains and books encode picoCTF{gr3p_15_m4g1c_ef8790dc}
```

# Solution

#### We can simply use `grep -r` to recursively search through every file for the `picoCTF{` pattern instead of manually inspecting thousands of files. The recursive search immediately reveals the file containing the flag together with the flag itself.

```
picoCTF{gr3p_15_m4g1c_ef8790dc}
```

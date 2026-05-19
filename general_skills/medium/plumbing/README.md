
# Overview
#### This challenge provides a remote service that continuously outputs thousands of lines of text through a network connection. Most of the lines are fake messages claiming they are not flags, but hidden somewhere in the huge output stream is the real flag. Since manually reading over 10,000 lines would be inefficient, the goal is to use shell piping and filtering utilities to automatically search the stream for the flag.

> *Description of **plumbing**:*
```
Sometimes you need to handle process data outside of a file.  
Can you find a way to keep the output from this program and search for the flag?

Connect fickle-tempest.picoctf.net 56713.
```

# Analysis

#### When connecting to the server using Netcat, the server continuously prints thousands of lines of junk output. Almost every line claims that it is not a flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# nc fickle-tempest.picoctf.net 56713
This is defintely not a flag
This is defintely not a flag
I don't think this is a flag either
Again, I really don't think this is a flag
Not a flag either
I don't think this is a flag either
Not a flag either
Again, I really don't think this is a flag
Again, I really don't think this is a flag
Again, I really don't think this is a flag
...
```

#### Since the challenge hints at handling process data outside of a file, this strongly suggests using shell pipes. Before searching for the flag, we can first check how much output the service produces.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# nc fickle-tempest.picoctf.net 56713 | wc -l
10002
```

#### The service outputs over 10,000 lines, so manually searching through the output would be tedious. Since picoCTF flags always contain the string `picoCTF`, we can simply pipe the output directly into `grep` to filter only lines containing the flag.

# Solution

#### Using shell pipes together with `grep`, we can automatically filter the massive output stream and immediately reveal the flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy]
└─# nc fickle-tempest.picoctf.net 56713 | grep pico
picoCTF{digital_plumb3r_8c8f3412}
```

# Flag

```
picoCTF{digital_plumb3r_8c8f3412}
```

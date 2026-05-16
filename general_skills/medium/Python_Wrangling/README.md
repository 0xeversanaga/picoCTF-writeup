# Overview

#### This challenge gives us a Python script named `ende.py` together with an encrypted file and a password file which already hints that the flag is encrypted and needs to be decrypted using the provided script. The goal of this challenge is basically to understand how the Python script works and use the correct password to decrypt `flag.txt.en` and reveal the flag.

> *Description of **Python Wrangling**:*
```
Python scripts are invoked kind of like programs in the Terminal...

Can you run ende.py using password.txt to get flag.txt.en?
```

> ***ende.py** contents:*
```
import sys
import base64
from cryptography.fernet import Fernet



usage_msg = "Usage: "+ sys.argv[0] +" (-e/-d) [file]"
help_msg = usage_msg + "\n" +\
        "Examples:\n" +\
        "  To decrypt a file named 'pole.txt', do: " +\
        "'$ python "+ sys.argv[0] +" -d pole.txt'\n"



if len(sys.argv) < 2 or len(sys.argv) > 4:
    print(usage_msg)
    sys.exit(1)



if sys.argv[1] == "-e":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "rb") as f:
        data = f.read()
        data_c = c.encrypt(data)
        sys.stdout.write(data_c.decode())


elif sys.argv[1] == "-d":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "r") as f:
        data = f.read()
        data_c = c.decrypt(data.encode())
        sys.stdout.buffer.write(data_c)


elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print(help_msg)
    sys.exit(1)


else:
    print("Unrecognized first argument: "+ sys.argv[1])
    print("Please use '-e', '-d', or '-h'.")
```

> ***flag.txt.en** contents:*
```
gAAAAABpRaHLJvQHNKx7S5bkBbCbLRygnKBNN2x32PTowWwOk2iIsCAgGdGgp_g-lIbghg4z6VSdljq5-moyXGu-5aQcrz5iaUEjHJWDAvd2xSZCeNVfUSJoUfj_wuZyjP3gQB5LdglQ
```

# Analysis

#### Looking at the Python script we can see that it supports both encryption and decryption using the `Fernet` module from the `cryptography` library. In this case the challenge asks us to decrypt the encrypted flag file which means we need to execute the script using the `-d` option together with the correct password.

```
elif sys.argv[1] == "-d":
    if len(sys.argv) < 4:
        sim_sala_bim = input("Please enter the password:")
    else:
        sim_sala_bim = sys.argv[3]

    ssb_b64 = base64.b64encode(sim_sala_bim.encode())
    c = Fernet(ssb_b64)

    with open(sys.argv[2], "r") as f:
        data = f.read()
        data_c = c.decrypt(data.encode())
        sys.stdout.buffer.write(data_c)
```

#### The challenge also provides a `password.txt` file which contains the decryption password needed by the script. Basically we just need to read the password file and enter it when the script prompts for it.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/Python_Wrangling]
└─# cat password.txt
720b6ad346f84cd483c60c7464dd95d4
```

# Solution

#### We can simply execute the Python script using the `-d` option followed by the encrypted file and then provide the password from `password.txt` when prompted. After successful decryption the script prints the plaintext flag directly to the terminal.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/Python_Wrangling]
└─# python3 ende.py -d flag.txt.en
Please enter the password:720b6ad346f84cd483c60c7464dd95d4
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
```

```
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
```

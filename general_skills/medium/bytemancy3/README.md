# Overview

#### Finishing `Bytemancy Series`, we have `bytemancy 3` as the last challenge. This is quite a huge leap from the previous challenge. We are given this binary named `spellbook` that consist of functions that are used in `app.py`. In this challenge the knowledge about [Endianness](https://en.wikipedia.org/wiki/Endianness) is required to solve.

> *Description of **bytemancy 3**:*

```
Can you conjure the right bytes? The program's source code can be downloaded here.

Connect to the program with netcat:
$ nc lonely-island.picoctf.net 59332
```

> *app.py with **line numbers**:*
```
001| import os
002| import random
003| import select
004| import sys
005| from typing import Optional
006| from pwn import ELF, p32
007| 
008| BANNER = "⊹──────[ BYTEMANCY-3 ]──────⊹"
009| BINARY_PATH = os.path.join(os.path.dirname(__file__), "spellbook")
010| QUESTION_COUNT = 3
011| 
012| SPELLBOOK_FUNCTIONS = [
013|     "ember_sigil",
014|     "glyph_conflux",
015|     "astral_spark",
016|     "binding_word",
017| ]
018| 
019| 
020| def read_exact_bytes(expected_len: int) -> Optional[bytes]:
021|     """Read a fixed number of bytes from stdin, trimming a trailing newline."""
022|     ...
045|     return buf
046| 
047| 
048| def main():
049|     try:
050|         elf = ELF(BINARY_PATH, checksec=False)
051|     except FileNotFoundError:
052|         print("The spellbook is missing!")
053|         return
054| 
055|     flag = open("./flag.txt", "r").read().strip()
056| 
057|     while True:
058|         try:
059|             print(BANNER)
060|             print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
061|             print()
062|             print("I will name four procedures hidden inside spellbook.")
063|             print(
064|                 f"Each round, send me their *raw* 4-byte addresses "
065|                 f"in little-endian form. {QUESTION_COUNT} correct answers unlock the flag."
066|             )
067|             print()
068|             print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
069|             print('⊹─────────────⟡─────────────⊹')
070| 
071|             selections = random.sample(SPELLBOOK_FUNCTIONS, QUESTION_COUNT)
072|             success = True
073| 
074|             for idx, symbol in enumerate(selections, 1):
075|                 target_addr = elf.symbols[symbol]
076|                 expected_bytes = p32(target_addr)
077| 
078|                 print(
079|                     f"[{idx}/{QUESTION_COUNT}] Send the 4-byte little-endian "
080|                     f"address for procedure '{symbol}'."
081|                 )
082|                 print("==> ", end='', flush=True)
083|                 user_bytes = read_exact_bytes(len(expected_bytes))
084| 
085|                 if user_bytes is None:
086|                     print("\nI needed four bytes, traveler.")
087|                     success = False
088|                     break
089| 
090|                 if user_bytes != expected_bytes:
091|                     print("\nThose aren't the right runes.")
092|                     success = False
093|                     break
094| 
095|             if success:
096|                 print(flag)
097|                 break
098| 
099|             print()
100|             print("The aether rejects your incantation. Try again.\n")
101|         except EOFError:
102|             break
103|         except Exception as exc:
104|             print(exc)
105|             break
106| 
107| 
108| if __name__ == "__main__":
109|     main()
```

# Analysis

#### There are 3 functions that is going to be randomly selected from the `SPELLBOOK_FUNCTIONS` list.
```
012| SPELLBOOK_FUNCTIONS = [
013|     "ember_sigil",
014|     "glyph_conflux",
015|     "astral_spark",
016|     "binding_word",
017| ]
```

#### We are asked to send the `4-byte little-endian` representation of the address for a chosen function. We need tackle what in the hell is a `little-endian` representation is.
```
077|                 ...
078|                 print(
079|                     f"[{idx}/{QUESTION_COUNT}] Send the 4-byte little-endian "
080|                     f"address for procedure '{symbol}'."
081|                 )
```

> *Endianness from **wikipedia**:*
```
In computing, endianness is the order in which bytes within a word data type are transmitted over a data
communication medium or addressed in computer memory, counting only byte significance compared to earliness.
Endianness is primarily expressed as big-endian (BE) or little-endian (LE).
```

#### The `little-endian` representation stores the least-significant byte at the smallest address.

> *Image from https://en.wikipedia.org/wiki/Endianness*
![endianness](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5d/32bit-Endianess.svg/500px-32bit-Endianess.svg.png)

#### A clear demonstration would be this in `Python`. The most significant byte which is `0xCA` is positioned last and least one at the first position. Now that we understand how `endianness` work, we move on to crafting the exploit that gets the address of the randomly chosen function, get the address of that function, submit the `little-endian` representation of the address.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/bytemancy3]
└─# python3
Python 3.13.3 (main, Apr 10 2025, 21:38:51) [GCC 14.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from struct import pack
>>> pack("<I", 0xCAFEF00D)
b'\r\xf0\xfe\xca'
```

#### We will use `pwntools` as also uses it by calling `p32()` which returns in default the little-endian representation of a given address `elf.symbols[symbol]`.
```
005| from typing import Optional
006| from pwn import ELF, p32
007| ...
073| ...............
074|             for idx, symbol in enumerate(selections, 1):
075|                 target_addr = elf.symbols[symbol]
076|                 expected_bytes = p32(target_addr)
077| ...................
```

# Solution

#### With this `Python` script we can get the flag and finally solve this challenge. We used `re` library in the `extract_func()` to get the randomly chosen function. And just get the address `addr = exe.sym[func]` then send the `little-endian` representation, repeat the process 3 times and them boom!

```
#!/usr/bin/env python3
from pwn import *
import re

context.log_level = "info"

HOST = 'green-hill.picoctf.net'
PORT = 59332

binary = "./spellbook"
exe = ELF(binary, checksec=False)

def start():
	return remote(HOST, PORT)

def extract_func(line):
	return re.search(rb"procedure '(\w+)'", line).group(1).decode()

def main():
	p = start()

	for i in range(3):
		data = p.recvuntil(b"==> ")
		func = extract_func(data)
		addr = exe.sym[func]

		info(f"{func} -> {hex(addr)}")
		p.send(p32(addr))

	p.interactive()

if __name__ == "__main__":
	main()
```

#### Running it gives us the flag!

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/medium/bytemancy3]
└─# python3 exploit.py REMOTE
[+] Opening connection to green-hill.picoctf.net on port 59332: Done
[*] binding_word -> 0x80491e3
[*] glyph_conflux -> 0x804919a
[*] ember_sigil -> 0x8049176
[*] Switching to interactive mode
picoCTF{0bjdump_m4g1c_e6e2de85}
[*] Got EOF while reading in interactive
$
```

```
picoCTF{0bjdump_m4g1c_e6e2de85}
```

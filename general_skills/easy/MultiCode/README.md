# Overview

#### This challenge is highly similar to `Undo` but with fewer gimmicks and just straight up gave the encoded flag.

> *Description of **MultiCode**:*
```
We intercepted a suspiciously encoded message, but it’s clearly hiding a flag.
No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?

Download the message.
```

# Analysis

#### After downloading the `message.txt` we're left with this. It seems from the challenge name `MultiCode` that this data is wrapped with multiple encoding. In the surface, we have this `base64` encoded text.

> *Reading `message.txt`:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/MultiCode]
└─# cat message.txt
NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjM0MzgzMTczMzAzNjM0NzAyNTM3NDQ=
```

#### Hmmm, this is kinda annoying, the characters are hex encoded. But we can work this out by using `bytes.fromhex()` from `Python`.

> *Base64 decoding `message.txt`:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/MultiCode]
└─# cat message.txt | base64 -d
637670625047532537426172666772715f72617030717661745f3438317330363470253744
```

#### Nice, I found a way to pipe everything and not have to write a whole script just to decode the flag. It seems the output is `URL encoded`, we can use the `urllib.parse.unqoute()` from `urllib` library to `URL decode`.

> *Hex decoding the Base64 decoded `message.txt`:*
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/MultiCode]
└─# cat message.txt | base64 -d | python3 -c "print(bytes.fromhex(input()).decode())"
cvpbPGS%7Barfgrq_rap0qvat_481s064p%7D
```

#### Now that it's `URL decoded`, we can observe the first `7 characters` and its familiar from [Undo](https://github.com/0xeversanaga/picoCTF-writeup/tree/main/general_skills/easy/Undo\#to-achieve-this-we-need-tr-to-replace-a-to-z-and-a-to-z-and-shift-the-position-to-n-to-za-to-m-and-n-to-za-to-m-we-can-do-this-by-providing-tr-a-za-z-n-za-mn-za-m-and-we-can-get-the-flag). It's the infamous `ROT13` cipher of `picoCTF`, it signifies that the alphabet of the output is rotated 13 items. So `A` becomes `N`, `Z` becomes `M` and it wraps through.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/MultiCode]
└─# cat message.txt | base64 -d | python3 -c "from urllib.parse import unquote;print(unquote(bytes.fromhex(input()).decode()))"
cvpbPGS{arfgrq_rap0qvat_481s064p}
```

# Solution

#### We can get the flag now by reversing the `ROT13` cipher using the `tr "A-Za-z" "N-ZA-Mn-za-m"` command.
```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/MultiCode]
└─# cat message.txt | base64 -d | python3 -c "from urllib.parse import unquote;print(unquote(bytes.fromhex(input()).decode()))" | tr "A-Za-z" "N-ZA-Mn-za-m"
picoCTF{nested_enc0ding_481f064c}
```

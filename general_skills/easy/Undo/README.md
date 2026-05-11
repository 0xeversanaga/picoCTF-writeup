# Overview

#### Another `easy` challenge. It asks us to use `netcat` or `nc` to connect to `foggy-cliff.picoctf.net`, on port `52357`.

> *Description of **Undo**:*
```
Can you reverse a series of Linux text transformations to recover the original flag?
Start searching for the flag here nc foggy-cliff.picoctf.net 52357
```

# Solution

#### Connecting to the server gives us this, it seems that we need to enter the command that reverses the encoded flag to recover it. `Step 1` hints us that the current flag is a base64 encoded string.
```
┌──(root💀lsd-AbsentRobust)-[~]
└─# nc foggy-cliff.picoctf.net 52357
===Welcome to the Text Transformations Challenge!===

Your goal: step by step, recover the original flag.
At each step, you'll see the transformed flag and a hint.
Enter the correct Linux command to reverse the last transformation.

--- Step 1 ---
Current flag: KTgxMzkzOW4zLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it:
```

> *To decode this base64 data we should enter `base64 -d`:*

```
--- Step 1 ---
Current flag: KTgxMzkzOW4zLWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
Hint: Base64 encoded the string.
Enter the Linux command to reverse it: base64 -d
Correct!
```

#### `Step 2` says we need to reverse the text. Using the command `rev` that reverses what is given in the input, we can achieve it.

```
--- Step 2 ---
Current flag: )813939n3-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
Hint: Reversed the text.
Enter the Linux command to reverse it: rev
Correct!
```

#### `Step 3` asks us to replace all `-` to `_`, we can achieve this by providing the command `tr '-' '_'`. The `tr` translates or delete characters from input.

```
--- Step 3 ---
Current flag: cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-3n939318)
Hint: Replaced underscores with dashes.
Enter the Linux command to reverse it: tr '-' '_'
Correct!
```

#### `Step 4` is the same but with 2 different characters. We can achieve this task by providing `()` and `{}` to the parameter for `tr`. The command would be `tr '()' '{}'`.

```
--- Step 4 ---
Current flag: cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_3n939318)
Hint: Replaced curly braces with parentheses.
Enter the Linux command to reverse it: tr '()' '{}'
Correct!
```

#### The last step, `Step 5` asks us to apply [ROT13](https://en.wikipedia.org/wiki/ROT13) to all letters. `ROT13` is a simple [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) where each letter is replaced by the letter 13 positions beyond it in the alphabet (wrapping at Z to A).

> ***ROT13*** *in action:*

```
a b c d e f g h i j k l m n o p q r s t u v w x y z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
n o p q r s t u v w x y z a b c d e f g h i j k l m
<-----------------------> <----------------------->
N - - - - - - - - - - - Z A - - - - - - - - - - - M
```

#### To achieve this, we need `tr` to replace `A to Z` and `a to z` and shift the position to `N to Z`:`A to M` and `n to z`:`a to m`. We can do this by providing `tr 'A-Za-z' 'N-ZA-Mn-za-m'` and we can get the flag!

```
--- Step 5 ---
Current flag: cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_3n939318}
Hint: Applied ROT13 to letters.
Enter the Linux command to reverse it: tr 'A-Za-z' 'N-ZA-Mn-za-m'
Correct!
```

#### Here goes the flag!

```
picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_3a939318}
```

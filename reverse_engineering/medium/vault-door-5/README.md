# Overview

#### Proceeding to `vault-door-5`, it seems we now have to deal with a different encoding method. This vault introduces us to [Percent-Encoding](https://en.wikipedia.org/wiki/Percent-encoding) AKA URL encoding and also [Base64 Encoding](https://en.wikipedia.org/wiki/Base64) which is a type of [binary-to-text encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding). A lot of references I know :3.

> *Source code with **line numbers**:*
```
01| import java.net.URLDecoder;
02| import java.util.*;
03|
04| class VaultDoor5 {
05|     public static void main(String args[]) {
06|      ...
16|     }
17|
18|     // Minion #7781 used base 8 and base 16, but this is base 64, which is
19|     // like... eight times stronger, right? Riiigghtt? Well that's what my twin
20|     // brother Minion #2415 says, anyway.
21|     //
22|     // -Minion #2414
23|     public String base64Encode(byte[] input) {
24|         return Base64.getEncoder().encodeToString(input);
25|     }
26|
27|     // URL encoding is meant for web pages, so any double agent spies who steal
28|     // our source code will think this is a web site or something, defintely not
29|     // vault door! Oh wait, should I have not said that in a source code
30|     // comment?
31|     //
32|     // -Minion #2415
33|     public String urlEncode(byte[] input) {
34|         StringBuffer buf = new StringBuffer();
35|         for (int i=0; i<input.length; i++) {
36|             buf.append(String.format("%%%2x", input[i]));
37|         }
38|         return buf.toString();
39|     }
40|
41|     public boolean checkPassword(String password) {
42|         String urlEncoded = urlEncode(password.getBytes());
43|         String base64Encoded = base64Encode(urlEncoded.getBytes());
44|         String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
45|                         + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
46|                         + "JTM0JTVmJTM0JTMxJTM4JTM1JTM1JTM1JTMxJTY1";
47|         return base64Encoded.equals(expected);
48|     }
49| }
```

# Analysis

#### The program has this convenience function `urlEncode()` and also `expected` is the base64 encoded data from output of `urlEncode()`. We just need to first, base64 decode `expected` and then url decode it to get the flag!

```
33|     public String urlEncode(byte[] input) {
34|      ...
39|     }
40|
41|     public boolean checkPassword(String password) {
42|     ...
44|         String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
45|                         + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
46|                         + "JTM0JTVmJTM0JTMxJTM4JTM1JTM1JTM1JTMxJTY1";
47|     ...
48|     }
```

# Solution

#### This `Python` script uses the library `base64` to decode `expected` and split the data using the delimiter `%`. And we're left with this list of hex data, after decoding and appending every hex we will get the flag.

```
import base64

def getFlag(b64encoded: list) -> str:
    flag_part = ""

    decoded = base64.b64decode(b64encoded).decode()

    hexes = decoded.split("%")[1:]

    for i in hexes:
        flag_part += chr(int(f"0x{i}", 16))

    return "picoCTF{" + flag_part + "}"

encoded = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTM0JTMxJTM4JTM1JTM1JTM1JTMxJTY1"

flag = getFlag(encoded)

print(flag)
```

#### And got the flag!

```
picoCTF{c0nv3rt1ng_fr0m_ba5e_64_4185551e}
```

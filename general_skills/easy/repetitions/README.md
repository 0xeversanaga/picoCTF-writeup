# Overview

#### This challenge gives us a file named `enc_flag` containing a very long encoded string and based on the challenge name `repetitions`, it already hints that some process was repeatedly done to the flag. The goal of this challenge is basically to identify what type of encoding was used and repeatedly decode it until we finally reveal the actual flag.

> *Description of **repetitions**:*
```
Can you make sense of this file?
Download the file here.
```

> ***enc_flag** contents:*
```
VmpGU1EyRXlUWGxTYmxKVVYwZFNWbGxyV21GV1JteDBUbFpPYWxKdFVsaFpWVlUxWVZaS1ZWWnVh
RmRXZWtab1dWWmtSMk5yTlZWWApiVVpUVm10d1VWZFdVa2RpYlZaWFZtNVdVZ3BpU0VKeldWUkNk
MlZXVlhoWGJYQk9VbFJXU0ZkcVRuTldaM0JZVWpGS2VWWkdaSGRXCk1sWnpWV3hhVm1KRk5XOVVW
VkpEVGxaYVdFMVhSbHBWV0VKVVZGWm9RMlZzV2tWUmJFNVNDbUpXV25wWmExSmhWMGRHZEdWRlZs
aGkKYlRrelZERldUMkpzUWxWTlJYTkxDZz09Cg==
```

# Analysis

#### Looking at the encoded contents we can immediately notice that it ends with `=` characters which is commonly used in `Base64` encoding padding. In this case the challenge name `repetitions` suggests that the data was encoded multiple times, which means we can repeatedly decode the output until we finally get the actual flag.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/repetitions]
└─# base64 -d enc_flag
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVX
bUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdW
MlZzVWxaVmJFNW9UVVJDTlZaWE1XRlpVWEJUVFZoQ2VsWkVRbE5SCmJWWnpZa1JhV0dGdGVFVlhi
bTkzVDFWT2JsQlVNRXNLCg==
```

#### After decoding it once we still get another encoded output which means the file was indeed repeatedly encoded using `Base64`.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/repetitions]
└─# base64 -d enc_flag | base64 -d
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVR
bHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFZUXBTTVhCelZEQlNR
bVZzYkRaWGFteEVXbm93T1VOblBUMEsK
```

#### Repeating the same decoding process several more times eventually reveals another encoded string and this confirms that the challenge is just nested `Base64` encoding done multiple times.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/repetitions]
└─# base64 -d enc_flag | base64 -d | base64 -d | base64 -d
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZa
R1psT0RBell6WjlDZz09Cg==
```

# Solution

#### We can simply repeatedly use the `base64 -d` command and pipe the output into another `base64 -d` until the actual flag appears. In this case the flag appeared after decoding the file six times which reveals the original plaintext contents.

```
┌──(root💀lsd-AbsentRobust)-[~/picoCTF-writeup/general_skills/easy/repetitions]
└─# base64 -d enc_flag | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dfe803c6}
```

```
picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_dfe803c6}
```

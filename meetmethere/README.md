# Meet Me There

In this challenge, we were given two files, `source.py` and `output.txt`.
By looking at `source.py`, we'll see that the encryption is fairly simple, it goes like this:
* Generate two key in the following format:
    * key1: `r'0{13}\p1\p2\p3'` where `\px` is a random character from `string.printable`
    * key2: `r'\p1\p2\p30{13}'` where `\px` is a random character from `string.printable`
* Encrypt the hex-encoded flag using `key1` in AES-ECB, let's call the output `flag_hex_enc`
* Encrypt the hex-encoded `flag_hex_enc` using `key2` in AES-ECB and outputing the result in hex

It's clear that we can bruteforce the keys, since there are only 3 unknown characters, and the length of `string.printable` is `100`, we'll end up with `1000000` possible values for each key, i'll take that all day, everyday.

So the exploit would be something like this:
1. try all possible values for `key2` until you get a hex-encoded output
2. try all possible values for `key1` until you get another hex-encoded output
3. decode to get flag

```
flag{y0u_m@d3_i7_t0_7h3_m1dddl3}
```
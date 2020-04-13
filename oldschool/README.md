# OldSchool

The challenge is made up of 2 parts, each one yields a part of the flag

## Part 1

we're given 3 files:
* a picture
* `Wqv Lvf xp "hnovIvo"`
* `hzdk{z_whg_mry_`

in the description they said that the one encrypted the flag used a method he learned in france, and since this is classical crypto, it's gotta be viginere or one of it's variants.

By messing around with the first text, i realised that it's a substitution cipher, with some intuition you get `Wqv Lvf xp == The Key is`, and we can notice that the flag is in flag format, meaning that `hzdk == flag`, we'll use this to get five letters of `hnovIvo`(because `v` is repeated twice), further more, `z` is a single word, meaning it can be either `a` or `i`, by using this, we can get the remaining letters:
* by using `hzdk == flag`, we can reverse-decrypt `hzdk` by using `flag` as key, which yields the original key `code`, so `hnoz == code`
* by using `z == i`, we get the fifth letter of the key in the same way as the other four, which is `R`, so the key so far is `codeRe*`, from here we can guess it, it's `codeRed`, we'll use it to decrypt the first part and we get 
```
flag{i_see_you_
```

## Part 2
for this part we're given an encoded string, the description for this part said that the flag was encoded twice with different encodings, and that the one who encoded the flag said *the average is 74.5*.
the encoded string is
```
=]e7A=>F&G@TRAe@9#X>=>OH3:,6Kp:,6I.=F*;T>"1M.;+PJ<Al1]S
```

thinking what the average is, i realised that it might be the sum of the bases used it the encoding divided by 2, so the sum of the bases used is `149`.

Looking at the encoded string, we can see that it contains `lowercase alphabet`, `uppercase alphabet`, `numbers` and `14 special characters`, so the total number of unique character used in this encoding is at least `26*3 + 10 + 14 == 76` characters, which reminded me of `base 85`, and by substracting `85` from `149` we get `64`, which made sense, so the first encoding is `base 85` and second is `base 64`, decoding the string yields
```
ar3_f@mili@r_w17h_7h3_0ld_w@y$}
```

so the flag is:
```
flag{i_see_you_ar3_f@mili@r_w17h_7h3_0ld_w@y$}
```

i didn't use the picture from the first part, but it turns out that it's used to decrypt that first text.
# Auto Bot

In this challenge, we're given a service `nc pwn.byteband.it 6000`.

The service provides us with a base64-encoded ELF file, the executable takes input, runs some processing on it, and compares it to a certain string, if they match, the service gives us another elf, else it prints `wrong password, lol` x)

After looking into the elf with `ghidra`, i realised how it works, it takes the input string and compares it to a fixed string, the comparison happens by comparing bytes in a certain order using an array of defined integers, for ex, the array is `[0x1, 0xf, 0x1b, 0x0a]`, the comparison goes by comparing the `input[0x1] to fixed_string[0]` then `input[0xf] to fixed_string[1]` and so on, so we just need to get the array and the static string, reconstruct the password and send it to the service.

I don't have good knowledge when it comes to ELF file structure, so i worked out of the usual for this one i think. so to get the `fixed_string`, i took a look at the binary of the ELF file, and i noticed that the `fixed_string` is in a pattern in the file, the pattern is `...\x00\x00fixed_string\x00Wrong pass...`, which means that by splitting the ELF file at `\x00Wrong pass` and splitting the first half at each `\x00`, we can get the `fixed_string` as it's gonna be the last element of the split result, as for the array on integers, i noticed in ghidra that the binary code for each array assignment falls into this pattern
`r'c7[8|4]5..f?f?f?f?f?f?(..)000000'`(everything in hex), so by grabbing all these patterns from the binary, it'll yield the array elements in order, and that's it. So each time you get an ELF file, you get grab the `fixed_string`, grab the array, reconstruct the password and send it to the service, repeat this until it sends the flag

```
flag{0pt1mus_pr1m3_has_chosen_you}
```
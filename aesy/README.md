# AESy

For this challenge, we were given a service `nc crypto.byteband.it 7004`, it gives us four options:
```
WELCOME TO ALICE's ENCRYPTION SERVICE
(Plaintext is hex-encoded before encryption)


1. Get your message encrypted.
2. Leave a message for Alice to decrypt.
3. Get Encrypted Flag.
4. Exit.
Enter your choice:
```

By encrypting some texts, i realised that there is padding, and the padding is applied after the text is hex-encoded, this seemed like a `cbc padding oracle` attack.

when you encrypt a message, it yield an `IV` plus the ciphertext, in the second choice, you can submit ciphertexts to `Alice`, by playing here a bit, i realised that it yields two things:
* `Alice: Got your message!!` if the ciphertext is good
* `Alice: Got your message??`, i got this when i flipped the last bit of the `IV`, and the ciphertext had padding, because the plaintext was `a`, so there is 14 bytes of padding, so i confirmed that it's a `CBC padding oracle`

I had a script that handles the attack from prior CTFs, i tweaked it to work with this service, and it worked
```
flag{th3_0racl3_0nly_gu1de$_7he_1337}
```
nice flag.
# Secure DES

So we're given a file `chall.py` and a service `nc crypto.byteband.it 7001`.

The encryption goes like this:
* Generate a prime `m`, and keep adding 1 to it until `m % 4 == 3` and `m` is prime
* Generate `l = [x for x in range(0, 1024, 8)]` and shuffle it
* Generate `l2`, a list containing `128` elements, where each element is `(key[i:i+8] + l[i]) ** 65536 % m` encoded in hex
* To encrypt, the service encrypt the plaintext `128` times, each time the key changes to `key[l[i]:l[i]+8]` and the output is the input of the next iteration

The service gives us 3 options:
* Encrypt String: encrypts a chosen plaintext
* Get Key: sends `m` and `l2`
* Get Encrypted Flag: sends encrypted flag in base64

In order to decrypt the flag, we must extract the keys from `l2`, here's what to do that:

So `m` is a prime, if we have `pow(msg, e, p) == ct` (where p is prime, e is exponent and msg is an int), then `pow(ct, e * inverse(e, p-1), p) == msg`, this is basically how RSA work, well, there is s small trick here, in fact, `pow(ct, e * inverse(e, p-1), p) == msg ** gcd(e, p-1)`, in RSA the `gcd` is 1, but in this challenge it's not, why? because `m % 4 == 3`, meaning that `m - 1` is an even number, and `65536` is also an even number, so the `gcd` is at least 2, this was basically the trick to this challenge, from here on it's simple:
* Calculate the `modular_inverse(65536, m-1)`, let's call it `d`
* Calculate `gcd(65536, m-1)`, let's call it `g`
* for each element `ct` of `l2`, calculate `root_of_the_gth_degree(pow(ct, d, m))` which yields `key[i:i+8] + l[i]`
* Reconstruct `key` and `l`
* Decrypt the flag in the `reversed` order

```
flag{y0u_f0und_th3_rar35t_ch33s3}
```
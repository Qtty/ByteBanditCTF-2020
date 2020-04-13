# RSyay!

For this challenge, we're given a script `source.py` running in `nc crypto.byteband.it 7002`.

The goal of the challenge is to encrypt given plaintexts using RSA xD, but for that we'll need `N` and `e`. Here what we have:
* `e == 65537`
* the service provides us with 3 values:
    * the plaintext in base64
    * `m`
    * `x`

the script first generates RSA keys, where the primes are n bits long, it also generates `m`, another prime with `n + 1` bits(this will prove to be crucial later).
It also generates an int `x`, where:
```python
x = pow(p, m, m)*pow(q, m, m) + p*pow(q, m, m) + q*pow(p, m, m) + p*q + pow(p, m-1, m)*pow(q, m-1, m)
```

our goal is to get `N`, let's dissect `x`:
`x` is made up of 6 terms so to say:
* `p`
* `q`
* `pow(p, m, m)`
* `pow(q, m, m)`
* `pow(p, m-1, m)`
* `pow(q, m-1, m)`

### pow(p, m-1, m) and pow(q, m-1, m)

From `Fermat's little theorem`:

*If p is prime and does not divide a, then a^(p – 1) ≡ 1 [p].*

since `m` is prime, and does not divide `p` nor `q`, then
```python
pow(p, m-1, m) == pow(q, m-1, m) == 1
```

### pow(p, m, m) and pow(q, m, m)
we have:
```python
pow(p, m, m) == pow(p, m-1, m) * pow(p, 1, m) # since p^m == p^(m-1) * p
             == 1 * pow(p, 1, m)
             == p # because m is 1 bit longer than p, so p won't wrap m, told ya it'll matter ;)
```
same goes for `q`, which means:
```python
pow(p, m, m) == p
pow(q, m, m) == q
```

### X
now we bring everything together:
```python
x == pow(p, m, m)*pow(q, m, m) + p*pow(q, m, m) + q*pow(p, m, m) + p*q + pow(p, m-1, m)*pow(q, m-1, m)
  == p*q + p*q + q*p + p*q + 1
  == 4*p*q + 1
  == 4*N + 1
```

### N
From now on it's simple, get the value of `x`, substract `1` and divide the result by `4`, the result in `N`, use it encrypt the plaintext

PS: the function `encrypt` used in the file is a bit out of the usual, check `solve.py` to see how does the encryption happens

```
flag{RSA_1s_th3_str0ng3st_c1ph3r_ind33d_0_0}
```
#!/usr/bin/python2

from socket import *
from Crypto.Util.number import inverse
from Crypto.Util.number import GCD as gcd
from gmpy2 import iroot
from Crypto.Cipher import DES


def tostr(n):
    x = pow(n, d, m)
    x = iroot(x, g)[0]
    assert pow(x, 65536, m) == n
    x = hex(x)[2:].rstrip('L')
    if len(x) % 2 != 0:
        x = '0' + x
    return x.decode('hex')

def decrypt(ct):
	for i in range(128):
		cipher = DES.new(key[l[127 - i]:l[127 - i] + 8], DES.MODE_ECB)
		ct = cipher.decrypt(ct)

	return ct

s = socket(AF_INET, SOCK_STREAM)
s.connect(('crypto.byteband.it', 7001))

s.recv(1024)
s.send('2\n')
x = s.recv(1024)
while ']' not in x:
    x += s.recv(1024)
m, l2 = x.split('\n')[:-1]

m = int(m, 16)
d = inverse(65536, m - 1)
g = gcd(65536, m-1)

l2 = eval(l2)
l2 = [tostr(eval(i)) for i in l2]

l = []
key = ''

for i in l2:
    key += i[:8]
    l.append(int(i[8:].encode('hex'), 16))

for i in l:
    assert i in [_ for _ in range(0, 1024, 8)]

s.send('3\n')
flag = s.recv(1024).split('\n')[0].decode('base64')
print decrypt(flag)
#!/usr/bin/python3

from socket import *
from base64 import b64decode, b64encode
from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA


s = socket(AF_INET, SOCK_STREAM)
s.connect(('crypto.byteband.it', 7002))
while True:
    x = s.recv(1024)
    print(x)
    x = x.split(b'\n')
    p = x[-6].split(b' ')[-1]
    n = eval(b'0x' + x[-4]) - 1
    assert n % 4 == 0
    n = n // 4

    key = RSA.RsaKey(e=65537, n=n)
    rsa = PKCS1_OAEP.new(key)
    p = rsa.encrypt(b64decode(p))
    s.send(b64encode(p) + b'\n')
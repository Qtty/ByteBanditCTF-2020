#!/usr/bin/python2

from string import printable
from itertools import product
from Crypto.Cipher import AES


def decrypt1(msg):
    keys = product(printable, repeat=3)
    for key in keys:
        print key
        aes = AES.new(key='0'*13 + ''.join(key), mode=AES.MODE_ECB)
        t = aes.decrypt(msg)
        try:
            print t.decode('hex')
            return t.decode('hex')
        except:
            pass

def decrypt2(msg):
    keys = product(printable, repeat=3)
    for key in keys:
        print key
        aes = AES.new(key=''.join(key) + '0'*13, mode=AES.MODE_ECB)
        t = aes.decrypt(msg)
        try:
            print t.decode('hex')
            return t.decode('hex')
        except:
            pass

ct = 'fa364f11360cef2550bd9426948af22919f8bdf4903ee561ba3d9b9c7daba4e759268b5b5b4ea2589af3cf4abe6f9ae7e33c84e73a9c1630a25752ad2a984abfbbfaca24f7c0b4313e87e396f2bf5ae56ee99bb03c2ffdf67072e1dc98f9ef691db700d73f85f57ebd84f5c1711a28d1a50787d6e1b5e726bc50db5a3694f576'.decode('hex')
ct = decrypt2(ct)
decrypt1(ct)

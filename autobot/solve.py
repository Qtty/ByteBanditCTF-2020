from socket import *
from os import system
from re import findall


def recvuntil(msg):
    x = s.recv(1024)
    print x
    while msg not in x:
        x += s.recv(1024)
    return x

s = socket(AF_INET, SOCK_STREAM)
s.connect(('pwn.byteband.it', 6000))
while True:
    elf = recvuntil('\n')
    print elf
    elf = elf.decode('base64')
    tar = elf.split('\x00Wrong pass')[0].split('\x00')[-1]
    l = findall(r'c7[8|4]5..f?f?f?f?f?f?(..)000000', elf.encode('hex'))
    l = [int(i, 16) for i in l]
    l = l[:l[-2]]
    pt = ''.join([tar[i] for i in l])
    print pt
    s.send(pt + '\n')
#!/usr/bin/python3

import socket
import random


def recvuntil(msg):
    x = s.recv(1024)
    while msg not in x:
        x += s.recv(1024)
    return x

server_info = 'crypto.byteband.it', 7004
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_info)
recvuntil(b'Enter your choice:')
s.send(b'3\n')
x = recvuntil(b'4.')
print (x.split(b'Here is your ciphertext(hex-encoded):\n')[1].split(b'\n')[0])
ct = bytearray.fromhex(x.split(b'Here is your ciphertext(hex-encoded):\n')[1].split(b'\n')[0].decode())

pt = ''
for j in range(0, len(x), 16):
    x = ct[j:j+32]
    plaintext = ''
    Z = []
    if len(x) == 32:
        for n in range(16):
            padding = n + 1
            payload = x.copy()

            payload[16-n:16] = bytearray(z ^ padding for z in reversed(Z))
            for byte in range(256):

                payload[15-n] = byte 
                s.send(b'2\n')
                recvuntil(b'ciphertext')
                s.send(payload.hex().encode() + b'\n')                        
                answer = recvuntil(b'Enter your choice:')
                print (answer.split(b'\n')[:3], byte, x[15-n], payload.hex().encode())
                if n == 0:
                    if b'!!' in answer and byte != x[15-n]:
                        z = byte ^ padding
                        letter = chr(z ^ x[15-n])
                        plaintext = letter + plaintext
                        Z.append(z)
                        print (list(plaintext), 1, len(plaintext))                                                       
                        break
                else:
                    if b'!!' in answer:
                        z = byte ^ padding
                        letter = chr(z ^ x[15-n])
                        plaintext = letter + plaintext
                        Z.append(z)
                        print (list(plaintext), 1, len(plaintext))                                                       
                        break
    pt += plaintext
print(plaintext)
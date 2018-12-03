import base64
from pwn import remote

init = 'A' * 15
known = ''
io = remote('127.0.0.1', 9000)
for i in range(16):
    io.sendline(init)
    base = io.recvline().decode()[:-1]
    base = base64.b64decode(base)[:16]

    for c in range(30, 128):
        io.sendline(init + known + chr(c))
        result = io.recvline().decode()[:-1]
        result = base64.b64decode(result)[:16]

        if result == base:
            known += chr(c)
            init = init[:-1]
            print(known)
            break
io.close()

import base64
from Crypto.Cipher import AES
import socket

key = 'Rnd_gen_pa55w0rd'
FLAG = 'FLAG{Some_C0Ol!}'


def encrypt(m):
    m += FLAG
    l = len(m)
    n = l // 16 + (1 if l % 16 != 0 else 0)
    return base64.b64encode(AES.new(key, AES.MODE_ECB).encrypt(m.ljust(n * 16, '\0')))


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9000))

while True:
    s.listen(1)
    conn, _ = s.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        data = data.decode()[:-1]
        conn.send(encrypt(data) + b'\n')
    conn.close()

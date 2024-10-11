import sys
import libnum
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

bits = 128
msg = "Hello"

if (len(sys.argv)>1):
        msg=str(sys.argv[1])
if (len(sys.argv)>2):
        bits=int(sys.argv[2])

p = getPrime(bits, randfunc=get_random_bytes)
q = getPrime(bits, randfunc=get_random_bytes)

n = p * q
PHI = (p - 1) * (q -1)
e = 65537
d = libnum.invmod(e, PHI)

m = bytes_to_long(msg.encode('utf-8'))

c = pow(m, e, n)
res = pow(c, d, n)


print(f"Message: {msg}")
print(f"p: {p}")
print(f"q: {q}")
print(f"d: {d}")
print(f"e: {e}")
print(f"n: {n}")
print(f"\nPrivate key: (d={d}, n={n})")
print(f"Public key: (e={e}, n={n})")
print(f"\nCipher: {c}")
print(f"Deciphered message: {long_to_bytes(res).decode('utf-8')}")
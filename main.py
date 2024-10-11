import sys
import Crypto
import libnum

bits = 128
message = "Hello"

msg = str(sys.argv[1])
bits = int(sys.argv[2])

p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

n = p * q
PHI = (p - 1) * (q -1)
e = 65537
d = libnum.invmod(e, PHI)



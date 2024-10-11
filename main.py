import sys
import libnum
from Crypto.Random import get_random_bytes
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

# Default key length for primes
key_size = 128
# Message to be encrypted and decrypted
message = "Hello"

# Override with command-line arguments if needed
if len(sys.argv) > 1:
    message = str(sys.argv[1])
if len(sys.argv) > 2:
    key_size = int(sys.argv[2])

# Generate prime numbers p and q
prime_p = getPrime(key_size, randfunc=get_random_bytes)
prime_q = getPrime(key_size, randfunc=get_random_bytes)

# Compute modulus n and Euler's totient (PHI)
modulus_n = prime_p * prime_q
totient_phi = (prime_p - 1) * (prime_q - 1)

# Public exponent (standard RSA value)
public_exponent_e = 65537

# Private exponent d (modular inverse of e modulo PHI)
private_exponent_d = libnum.invmod(public_exponent_e, totient_phi)

# Convert the message to a number (plaintext)
plaintext_m = bytes_to_long(message.encode('utf-8'))

# Encrypt the plaintext to produce the ciphertext
ciphertext_c = pow(plaintext_m, public_exponent_e, modulus_n)

# Decrypt the ciphertext to recover the plaintext
decrypted_m = pow(ciphertext_c, private_exponent_d, modulus_n)

# Print results
print(f"Original message: {message}")
print(f"Prime p: {prime_p}")
print(f"Prime q: {prime_q}")
print(f"Modulus n (p * q): {modulus_n}")
print(f"Euler's Totient (phi): {totient_phi}")
print(f"Public exponent (e): {public_exponent_e}")
print(f"Private exponent (d): {private_exponent_d}")
print(f"\nPrivate key: (d={private_exponent_d}, n={modulus_n})")
print(f"Public key: (e={public_exponent_e}, n={modulus_n})")
print(f"\nCiphertext: {ciphertext_c}")
print(f"Decrypted message: {long_to_bytes(decrypted_m).decode('utf-8')}")

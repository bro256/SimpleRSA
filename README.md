# RSA Encryption/Decryption in Python

This is a Python program that demonstrates a basic implementation of RSA encryption and decryption using core building blocks like prime number generation, modular arithmetic, and modular exponentiation. The program uses the RSA algorithm to encrypt and decrypt a message.

## Features

- **Manual RSA Key Generation**: Generates RSA keys by computing two large primes, `p` and `q`, each sized at half the specified key length so the resulting modulus matches the target key size.
- **Encryption**: Encrypts a message using the public key `(e, n)`.
- **Decryption**: Decrypts the ciphertext back to the original message using the private key `(d, n)`.
- **Custom Key Size**: Allows for changing the RSA key size (in bits) by providing it as a command-line argument.
- **Message Length Check**: Verifies that the message is small enough to be encrypted with the generated key size.
- **Automatic Retry**: If the public exponent `e` happens not to be invertible modulo `phi` for a given prime pair (a rare edge case), the program regenerates `p` and `q` automatically.

## Requirements

The program uses the following libraries:

- [PyCryptodome](https://pypi.org/project/pycryptodome/) for random prime number generation.
- [libnum](https://pypi.org/project/libnum/) for modular inverse computation.

> **Note:** `libnum` is a small, lightly-maintained third-party package. If you run into installation issues, check that your Python version is compatible, or consider swapping in `pow(e, -1, phi)` (Python 3.8+) as a drop-in replacement for `libnum.invmod`.

To install the dependencies, use:

```bash
pip install -r requirements.txt
```

## Running the Program
To run the program, use:
```bash
python rsa.py [message] [key_size]
```
- **message**: The message to be encrypted (optional, default is "Hello").
- **key_size**: The total size of the RSA modulus `n` in bits (optional, default is 2048 bits).

## How It Works

### Key Generation

The program generates two large prime numbers, `p` and `q`, each `key_size // 2` bits long, using the `getPrime` function from the PyCryptodome library — this ensures the product `n = p * q` lands at approximately the specified `key_size`, rather than double it. Euler's totient, `phi`, is calculated as `(p-1) * (q-1)`. The public exponent `e` is set to the standard value `65537`, and the private exponent `d` is computed as the modular inverse of `e` modulo `phi` using `libnum.invmod`. If `e` and `phi` are not coprime (rare but possible), the program discards the pair and regenerates new primes until it finds a valid one.

### Encryption

1. The message to be encrypted is first converted from a string to a number using `bytes_to_long` from PyCryptodome.
2. The ciphertext is computed using the formula `ciphertext = plaintext^e % n` where `e` is the public exponent and `n` is the modulus.

### Decryption

1. The ciphertext is decrypted using the private key by calculating `plaintext = ciphertext^d % n`, where `d` is the private exponent.
2. The decrypted number is converted back to the original message string using `long_to_bytes`.

### Customization

- The program allows you to pass a custom message and key size as command-line arguments.
- By default, the key size is set to 2048 bits (the size of the resulting modulus `n`), but you can specify a different value to experiment with smaller or larger keys. Be aware that larger keys will take more time to generate and use more resources.

### Limitations

- **Educational use only.** This implementation is meant to illustrate how RSA works internally, not for securing real data.
- The RSA algorithm can only encrypt messages that are smaller than the modulus `n`. If the message is too large, an error is printed — there's no chunking or multi-block support.
- This implementation does not include padding schemes (e.g., OAEP), which are essential for secure encryption in real-world scenarios. Without padding, this implementation is vulnerable to standard textbook-RSA attacks.
- Key generation time increases significantly at larger key sizes (4096-bit and above), since generating large primes is computationally expensive.

## Example Output

Here's an example of the output when running the program with the default message and key size:

```
Original message: Hello
Prime p: 287920137794493974756253142172408919076383720859348999358716536605509491358932152401898965081378223252750901107176233139251943759204673933305617899308435046522192116771
Prime q: 332777258394139274527034105801754035137526752728051073701583060784085476791369541451053705518097827627214907668327235870946165748491408768885573392603255070593826285459
Modulus n (p * q): 957677268622689680712147609094597684963690787905041410707003900457179691229166157983487574353473564008337775672785070683836705195678594973594931249269177973826838025484...
Euler's Totient (phi): 957677268622689680712147609094597684963690787905041410707003900457179691229166157983487574353473564008337775672785070683836705195678594973594931249269177973826837403689...
Public exponent (e): 65537
Private exponent (d): 860672107445225165392693980353119959963899164655310360688399451857284412467337707215643602348759491158567604562649617398879896698205297659812351467757630446788846277510...
Ciphertext: 184323842987372470646343847799286601533265442796563962707143327110496877611479706299659451785641743066822673902362114697898690907736876843076852719285021203190191051188...
Decrypted message: Hello
```
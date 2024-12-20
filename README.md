# RSA Encryption/Decryption in Python

This is a Python program that demonstrates a basic implementation of RSA encryption and decryption using core building blocks like prime number generation, modular arithmetic, and modular exponentiation. The program uses the RSA algorithm to encrypt and decrypt a message.

## Features

- **Manual RSA Key Generation**: Generates RSA keys by computing large prime numbers `p` and `q`.
- **Encryption**: Encrypts a message using the public key `(e, n)`.
- **Decryption**: Decrypts the ciphertext back to the original message using the private key `(d, n)`.
- **Custom Key Size**: Allows for changing the RSA key size by providing it as a command-line argument.
- **Message Length Check**: Verifies that the message is small enough to be encrypted with the generated key size.

## Requirements

The program uses the following libraries:

- [PyCryptodome](https://pypi.org/project/pycryptodome/) for random prime number generation.
- [libnum](https://pypi.org/project/libnum/) for modular inverse computation.

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
- **key_size**: The size of the RSA key in bits (optional, default is 2048 bits).

## How It Works

### Key Generation

The program begins by generating two large prime numbers, `p` and `q`, using the `getPrime` function from the PyCryptodome library. The product of these two primes, `n`, is used as the modulus in both the public and private keys. The Euler’s totient function, `phi`, is calculated as `(p-1) * (q-1)`. The public exponent `e` is set to the common value `65537`, and the private exponent `d` is calculated as the modular inverse of `e` modulo `phi` using the `invmod` function from the libnum library.

### Encryption

1. The message to be encrypted is first converted from a string to a number using `bytes_to_long` from PyCryptodome.
2. The ciphertext is computed using the formula `ciphertext = plaintext^e % n` where `e` is the public exponent and `n` is the modulus.

### Decryption

1. The ciphertext is decrypted using the private key by calculating `plaintext = ciphertext^d % n`, where `d` is the private exponent.
2. The decrypted number is converted back to the original message string using `long_to_bytes`.

### Customization

- The program allows you to pass a custom message and key size as command-line arguments.
- By default, the key size is set to 2048 bits, but you can specify a different key size to experiment with smaller or larger keys. Be aware that larger keys will take more time to generate and use more resources.

### Limitations

- The RSA algorithm can only encrypt messages that are smaller than the modulus `n`. If the message is too large, an error is printed.
- This implementation does not include padding schemes (e.g., OAEP) that are essential for secure encryption in real-world scenarios.

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
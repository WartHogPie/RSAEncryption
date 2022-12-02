# RSAEncryption
RSA encryption is a theorietically unbreakable form of encryption used by government agencies and big computer companies across the world because of its intense security.

## How it works
To understand RSA, you must understand the modulus function. The modulus function spits out the remainder after dividing two numbers, and is rather easy to compute with small numbers, but it gets harder the larger the numbers get. For instance, 9 mod 2 is 1 because if you divide 9 by 2, the quotient is 4 and the remainder is 1. The modulus function is represented by a % sign in Python.

RSA works by finding a number that, when the modulus of it and the key is taken, equals the input number. For example:

The input number is 2 and the key is 8. The RSA algorithm finds that the modulus of 514 and the key, 8, is 2, so the encrypted number is 514.

The complexity of an RSA key is determined by how many bits it has. 8 has 4 bits because its binary representation is 1000. This example is pretty easy to crack with a moderate computer because the key is only 4-bit, but the higher the number of bits in a key, the harder it will be to crack, until it is unreasonable to even attempt to crack it.

## How to use it
The class RSAEncryption takes three positional arguments on initialization. They are as follows:

bin_key: The binary key to use in encryption and decryption. Set to None to either generate or load a key instead
bits: The number of bits the generated binary key will be. Set above 2048 at your own risk.
load_key: Set to True to load a binary key from 'key.txt' in the cwd, and False to generate a new key if bin_key is set to None. This is useful for large copy-paste binary keys and keeping persistent keys between program runs.
#
The class also has the following methods:

save_key(): Saves the current key to 'key.txt', overwriting the old file if it exists.
###
load_key(): Loads a key from 'key.txt', overwriting the existing key if there is one.
###
regenerate_key(): Generates a new key with the number of bits specified in the init.
###
encrypt(int a): For use internally. Returns the number 'a' encrypted with the current binary key.
###
decrypt(int a): For use internally. Returns the number 'a' decrypted with the current binary key.
###
encrypt_string(str a): Accepts any string 'a'. Returns a string of comma-separated numbers, each are the ASCII letters in the string 'a', encrypted with the current binary key.
###
decrypt_string(str a): Accepts a string of comma-separated numbers 'a'. Returns a plaintext string decrypted with the current binary key.

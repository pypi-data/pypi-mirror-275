"""
Cryptographic applications library based on elliptic curve cryptography.
Can be used for asymmetric and symmetric cryptography, signature verification,
and supports password-secured cryptography.
Built on the eciespy, coincurve and hashlib modules.
"""

import hashlib
import os
import traceback
from ecies.utils import generate_key
import ecies
import coincurve
from cryptography.fernet import Fernet


class Crypt:
    """Encryption/decryption engine for bytearrays.
    Can be used for single-session public-key/private-key cryptography
    as well as for password secured multi-session public-key/private-key or private-key-only cryptography.
    * Single-session means the keys are used only as long as the Crypt instance exists,
    * so when the program is restarted different keys are used.
    * Multi-session means that the same keys can be reused after restarting the program,
    * a simplified form of the private key must be memorised by the useras a password.
    Usage:
        - As Single-Session Asymetric Encryption System (public-key and private-key):
            # Communication Receiver:
            codec = Crypt()
            public_key = codec.public_key

            ## give public_key to Sender

            # Communication Sender:
            codec2 = Encryptor(public_key)
            cipher = codec2.encrypt("Hello there!".encode('utf-8'))

            ## transmit cipher to Receiver

            # Communication Receiver:
            plaintext = codec.decrypt(cipher).decode('utf-8')

        - As Multi-Session Asymetric Encryption System (public-key and private-key):
            # Communication Receiver:
            codec = Crypt("mypassword")   # KEEP PASSWORD PRIVATE AND SAFE
            public_key = codec.public_key

            ## give public_key to Sender

            # Communication Sender:
            codec2 = Encryptor(public_key)
            cipher = codec2.encrypt("Hello there!".encode('utf-8'))

            ## transmit cipher to Receiver

            # Communication Receiver:
            plaintext = codec.decrypt(cipher).decode('utf-8')


        - As Multisession Symetric Enryption System (private-key only):
            codec = Crypt("my_password")   # KEEP PASSWORD PRIVATE AND SAFE
            cipher = codec.encrypt("Hello there!".encode('utf-8'))

            ## transmit cipher to other person

            codec2 = Crypt("my_password")
            plaintext = codec2.decrypt(cipher).decode('utf-8')
    """

    public_key = ""  # string
    __private_key = ""  # coincurve.keys.coincurve.PrivateKey

    def __init__(self, password=None, private_key=None):
        if not password and not private_key:
            key = generate_key()    # generate new random key
        elif password:
            # creating a cryptographic hash from the password, to create a larger encryption key from it
            hashGen = hashlib.sha256()
            hashGen.update(password.encode())
            hash = hashGen.hexdigest()

            key = coincurve.PrivateKey.from_hex(hash)
        elif private_key:
            key = coincurve.PrivateKey.from_hex(private_key)
        else:
            raise Exception("Specify a password or a private_key, not both.")

        self.__private_key = key
        self.public_key = key.public_key.format(False).hex()

    def encrypt(self, data_to_encrypt: bytearray):
        return encrypt(data_to_encrypt, self.public_key)

    def decrypt(self, encrypted_data: bytearray):
        return decrypt(encrypted_data, self.__private_key)

    def encrypt_file(self, plain_file, encrypted_file):
        return encrypt_file(plain_file, encrypted_file, self.public_key)

    def decrypt_file(self, encrypted_file, decrypted_file):
        return decrypt_file(encrypted_file, decrypted_file, self.__private_key)

    def sign(self, data: bytes):
        return sign(data, self.__private_key)

    def verify_signature(self, data: bytes, signature: bytes):
        return verify_signature(data, self.public_key, signature)

    def get_private_key(self):
        """Returns the private key in hexadecimal format."""
        return self.__private_key.to_hex()

    def get_public_key(self):
        """Returns the private key in hexadecimal format."""
        return self.__private_key.to_hex()


class Encryptor:
    def __init__(self, public_key):
        self.public_key = public_key

    def encrypt(self, data):
        return encrypt(data, self.public_key)

    def encrypt_file(self, plain_file, encrypted_file):
        return encrypt_file(plain_file, encrypted_file, self.public_key)

    def verify_signature(self, data, signature):
        return verify_signature(data, self.public_key, signature)


def encrypt(data_to_encrypt: bytearray, public_key):
    """Encryption-only engine for bytearrays, based on public-key.
    Usage:
        # Communication Receiver:
        codec = Crypt()
        public_key = codec.public_key

        ## give public_key to Sender

        # Communication Sender:
        cipher = encrypt("Hello there!".encode('utf-8'), public_key)

        ## transmit cipher to Receiver

        # Communication Receiver:
        plaintext = codec.decrypt(cipher).decode('utf-8')
    """
    try:
        if isinstance(data_to_encrypt, str):
            print("data to encrypt must be of type bytearray")
        if isinstance(public_key, bytearray):
            public_key = public_key.hex()
        encrypted_data = ecies.encrypt(public_key, data_to_encrypt)
        return encrypted_data
    except Exception as e:
        print("Failed at encryption.")
        print(e)
        print("----------------------------------------------------")
        traceback.print_exc()  # printing stack trace
        print("----------------------------------------------------")
        print("")
        print("public key: " + public_key)
        print("")
        return None


def decrypt(encrypted_data: bytearray, private_key: bytearray):
    try:
        if isinstance(private_key, coincurve.keys.PrivateKey):
            key = private_key.to_hex()
        elif isinstance(private_key, bytearray):
            key = private_key.hex()
        elif isinstance(private_key, str):
            key = private_key

        if(type(encrypted_data) == bytearray):
            encrypted_data = bytes(encrypted_data)
        decrypted_data = ecies.decrypt(
            key, encrypted_data)
        return decrypted_data
    except Exception as e:
        print("Failed at decryption.")
        print(e)
        print("----------------------------------------------------")
        traceback.print_exc()  # printing stack trace
        print("----------------------------------------------------")
        print("")
        # print(encrypted_data)
        return None


def sign(data: bytes, private_key: bytearray):
    if isinstance(private_key, coincurve.keys.PrivateKey):
        key = private_key
    elif isinstance(private_key, bytearray):
        key = coincurve.PrivateKey.from_hex(private_key.hex())
    elif isinstance(private_key, str):
        key = coincurve.PrivateKey.from_hex(private_key)
    return key.sign(data)


def verify_signature(data: bytes, public_key: bytes, signature: bytes):
    if isinstance(public_key, str):
        public_key = bytes(bytearray.fromhex(public_key))
    elif isinstance(data, bytearray):
        public_key = bytes(public_key)
    if isinstance(data, bytearray):
        data = bytes(data)
    if isinstance(signature, bytearray):
        signature = bytes(signature)
    return coincurve.verify_signature(signature, data, public_key)


def encrypt_file(plain_file, encrypted_file, public_key):
    """
    encrypt a file.
    Parameters:
        plain_file: the path of the file to encrypt
        encrypted_file: where the encrypted file should be saved
    """
    key = Fernet.generate_key()
    f = Fernet(key)

    with open(plain_file, 'rb') as file:
        plain_data = file.read()
    encrypted_data = f.encrypt(plain_data)

    key_encrypted = encrypt(key, public_key)

    encrypted_data = key_encrypted + encrypted_data
    with open(encrypted_file, 'wb') as file:
        file.write(encrypted_data)


def decrypt_file(encrypted_file, decrypted_file, private_key: bytearray):

    with open(encrypted_file, 'rb') as file:
        encrypted_data = file.read()
    key = encrypted_data[:141]   # extract encrypted key from file
    encrypted_data = encrypted_data[141:]    # remove encrypted key from file

    # decrypt encrypted key and create file-decrypting Fernet object from it
    f = Fernet(decrypt(key, private_key))

    decrypted_data = f.decrypt(encrypted_data)  # decrypt file

    with open(decrypted_file, 'wb') as file:
        file.write(decrypted_data)

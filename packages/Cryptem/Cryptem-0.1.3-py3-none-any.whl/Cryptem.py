"""
Cryptographic applications library based on elliptic curve cryptography.
Can be used for asymmetric and symmetric cryptography, signature verification,
and supports password-secured cryptography.
Built on the eciespy, coincurve and hashlib modules.
"""
from cryptem import Crypt, Encryptor, encrypt, encrypt_file, verify_signature
from termcolor import colored

print(colored("Cryptem: DEPRECATED: The Cryptem module has been renamed to cryptem to accord with PEP 8 naming conventions.", "yellow"))


def CryptEncrypt(self, data_to_encrypt: bytearray):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.Encrypt) has been renamed to cryptem.Crypt.encrypt to accord with PEP 8 naming conventions.", "yellow"))

    return self.encrypt(data_to_encrypt)


def CryptDecrypt(self, encrypted_data: bytearray):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.Decrypt) has been renamed to cryptem.Crypt.decrypt to accord with PEP 8 naming conventions.", "yellow"))
    return self.decrypt(encrypted_data)


def CryptEncryptFile(self, plain_file, encrypted_file):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.EncryptFile) has been renamed to cryptem.Crypt.encrypt_file to accord with PEP 8 naming conventions.", "yellow"))
    return self.encrypt_file(plain_file, encrypted_file)


def CryptDecryptFile(self, encrypted_file, decrypted_file):

    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.DecryptFile) has been renamed to cryptem.Crypt.decrypt_file to accord with PEP 8 naming conventions.", "yellow"))
    return self.decrypt_file(encrypted_file, decrypted_file)


def CryptSign(self, data: bytes):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.Sign) has been renamed to cryptem.Crypt.sign to accord with PEP 8 naming conventions.", "yellow"))
    return self.sign(data)


def CryptSignSmall(self, data: bytearray):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.SignSmall) has been removed.", "red"))


def CryptVerifySignature(self, data: bytes, signature: bytes):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Crypt.VerifySignature) has been renamed to cryptem.Crypt.verify_signature to accord with PEP 8 naming conventions.", "yellow"))
    return self.verify_signature(data, signature)


Crypt.Encrypt = CryptEncrypt
Crypt.Decrypt = CryptDecrypt
Crypt.EncryptFile = CryptEncryptFile
Crypt.DecryptFile = CryptDecryptFile
Crypt.Sign = CryptSign
Crypt.SignSmall = CryptSignSmall
Crypt.VerifySignature = CryptVerifySignature


def EncryptorEncrypt(self, data):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Encryptor.Encrypt) has been renamed to cryptem.Encryptor.encrytp to accord with PEP 8 naming conventions.", "yellow"))
    return self.encrypt(data)


def EncryptorEncryptFile(self, plain_file, encrypted_file):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Encryptor.EncryptFile) has been renamed to cryptem.Encryptor.encrypt_file to accord with PEP 8 naming conventions.", "yellow"))
    return self.encrypt_file(plain_file, encrypted_file)


def EncryptorVerifySignature(self, data, signature):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Encryptor.VerifySignature) has been renamed to cryptem.Encryptor.verify_signature to accord with PEP 8 naming conventions.", "yellow"))
    return self.verify_signature(data, signature)


Encryptor.Encrypt = EncryptorEncrypt
Encryptor.EncryptFile = EncryptorEncryptFile
Encryptor.VerifySignature = EncryptorVerifySignature


def Encrypt(data_to_encrypt: bytearray, public_key):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.Encrypt) has been renamed to cryptem.encrypt to accord with PEP 8 naming conventions.", "yellow"))
    return encrypt(data_to_encrypt, public_key)


def EncryptFile(plain_file, encrypted_file, public_key):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.EncryptFile) has been renamed to cryptem.encrypt_file to accord with PEP 8 naming conventions.", "yellow"))
    return encrypt_file(plain_file, encrypted_file, public_key)


def VerifySignature(data: bytes, public_key: bytes, signature: bytes):
    print(colored("Cryptem: DEPRECATED: This function (Cryptem.VerifySignature) has been renamed to cryptem.verify_signature to accord with PEP 8 naming conventions.", "yellow"))
    return verify_signature(data, public_key, signature)

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from binascii import hexlify


def encrypt(publicKeyString, content):
    publicKey = RSA.import_key(publicKeyString)
    encryptor = PKCS1_OAEP.new(key=publicKey)
    crypticContent = encryptor.encrypt(content)
    return crypticContent


def decrypt(privateKeyString, crypticContent):
    privateKey = RSA.import_key(privateKeyString)
    decryptor = PKCS1_OAEP.new(key=privateKey)
    content = decryptor.decrypt(crypticContent)
    return content

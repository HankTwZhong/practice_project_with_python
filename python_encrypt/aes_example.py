import base64
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


AES_SECRET_KEY ='B32159863156DADJ'

IV = 'CMHDKSDJAFIEKLFA'

BS = len(AES_SECRET_KEY)

pad = lambda s: s+(BS-len(s) % BS) * chr(BS-len(s) % BS)
unpad = lambda s:s[0:-ord(s[-1])]

class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        ## Text length must be multiple of 16
        cryptor = AES.new(self.key, self.mode, self.key)
        length = 16
        count = len(text)
        if (count %  length != 0):
            add = length - (count % length)
        else:
            add = 0
            text = text + ('\0' * add)
            self.ciphertext = cryptor.encrypt(text)
            return b2a_hex(self.ciphertext)

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(a2b_hex(text))
        return plain_text

if __name__ == '__main__':
    aesency = AES_ENCRYPT()
    encrypt_character = aesency.encrypt('forsomereason123')
    descrypt_character = aesency.decrypt(encrypt_character)
    print(encrypt_character)
    print(descrypt_character)
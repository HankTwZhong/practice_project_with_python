import base64
from Crypto.Cipher import AES


AES_SECRET_KEY ='B32159863156DADJ'

IV = 'CMHDKSDJAFIEKLFA'

BS = len(AES_SECRET_KEY)

pad = lambda s: s+(BS-len(s) % BS) * chr(BS-len(s) % BS)
unpad = lambda s:s[0:-ord(s[-1])]

class AES_ENCRYPT(object):
    def __init__(self):
        self.key = AES_SECRET_KEY
        self.mode = AES.MODE_CBC

    



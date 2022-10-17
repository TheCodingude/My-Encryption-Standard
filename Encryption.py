import string
from cryptography.fernet import Fernet

class Encrypt:

    def __init__(self, key: string) -> None:
        self.key = key[1:]
        self.shift = int(key[0])
        self.letters = string.ascii_letters + string.punctuation + string.digits
        self.shifted = self.letters[(s := self.shift):] + self.letters[:s]
        print(len(self.letters))

    def encrypt(message: str) -> str:
        pass

    def __CaeserEncrypt(message):
        pass

    def decrypt(message: str) -> str:
        pass

    def __CaeserDecrypt(message): 
        pass

Encrypt("3Kdmopsm!l2mrkqavn7(na%")
# 94
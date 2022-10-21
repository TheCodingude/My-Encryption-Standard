import string
import random
from cryptography.fernet import Fernet

class Encrypt:

    def __init__(self, key: string) -> None:
        self.key = key[2:]
        self.shift = int(key[:2])
        self.letters = string.ascii_letters + string.punctuation + string.digits
        self.shifted = self.letters[(s := self.shift):] + self.letters[:s]
        self.fernet = Fernet(self.key)


    def createKey() -> str:

        choice = []
        key = Fernet.generate_key()
        key = key.decode()
        list = [10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
        choice.append(random.choice(list))
        choice.append(random.choice(list))
        choice.append(random.choice(list))
        choice.append(random.choice(list))
        final = random.choice(choice)
        return str(final) + key

    def encrypt_key():
        pass



    def encrypt(self, message: str) -> str:
        self.message = message.encode()
        self.encrypted = self.fernet.encrypt(self.message)
        self.encrypted = self.CaeserEncrypt(self.encrypted)
        return self.encrypted


    def CaeserEncrypt(self, message: str):
        message = message.decode()
        table = str.maketrans(self.letters, self.shifted)
        scrambled = message.translate(table)
        return scrambled

    def decrypt(self, message: str) -> str:
        self.decrypted =  self.__CaeserDecrypt(message)
        self.decrypted = self.fernet.decrypt(self.decrypted)
        return self.decrypted.decode()


    def __CaeserDecrypt(self, message: str): 
        table = str.maketrans(self.shifted, self.letters)
        unscrambled = message.translate(table)
        return unscrambled.encode()


key = Encrypt.createKey()
e = Encrypt(key)
print("key: " + key)
encrypted = e.encrypt("This is yes")
print("en: " + encrypted)
decrypted = e.decrypt(encrypted)
print("de: " + decrypted)

#change the numbers to letters for better hiding
#have different shift for begining letters since the are always the same
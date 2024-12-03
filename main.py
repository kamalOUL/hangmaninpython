import string
import random

chars= " " + string.digits + string.punctuation + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key  : {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"original text: {plain_text}")
print(f"Cipher text  : {cipher_text}")

#DECRYPT

cipher_text1 = input("Enter a message to decrypt: ")
paint_text1 = ""

for x in cipher_text1:
    index1 = key.index(x)
    paint_text1 += chars[index1]
print(f"decrypted text: {cipher_text1}")
print(f"original text : {paint_text1}")
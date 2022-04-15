from random import choice
from string import ascii_letters
from string import ascii_uppercase
from string import ascii_lowercase


def encrypt_by_vernam_yourself(input_for_encrypt, key_word):  # encrypting by your own keyword
    encrypted = ""
    for i in range(len(input_for_encrypt)):
        char = input_for_encrypt[i]
        key_char = key_word[i % len(key_word)]
        encrypted += chr(ord(char) ^ ord(key_char))
    return encrypted


def encrypt_by_vernam(input_for_encrypt):  # encrypting by generated keyword
    encrypted = ""
    if input_for_encrypt.isupper():
        key_word = (''.join(choice(ascii_uppercase) for i in range(len(input_for_encrypt))))
    elif input_for_encrypt.islower():
        key_word = (''.join(choice(ascii_lowercase) for i in range(len(input_for_encrypt))))
    else:
        key_word = (''.join(choice(ascii_letters) for i in range(len(input_for_encrypt))))
    for i in range(len(input_for_encrypt)):
        char = input_for_encrypt[i]
        key_char = key_word[i % len(key_word)]
        encrypted += chr(ord(char) ^ ord(key_char))
    return encrypted, "\n\nGenerated keyword is: " + str(key_word)


def decrypt_by_vernam_yourself(input_for_decrypt, key_word):  # decrypting by known keyword
    decrypted = ""
    for i in range(len(input_for_decrypt)):
        char = input_for_decrypt[i]
        key_char = key_word[i % len(key_word)]
        decrypted += chr(ord(char) ^ ord(key_char))
    return decrypted


def decrypt_by_vernam(input_for_decrypt):  # decrypting by generated keyword
    decrypted = ""
    if input_for_decrypt.isupper():
        key_word = (''.join(choice(ascii_uppercase) for i in range(len(input_for_decrypt))))
    elif input_for_decrypt.islower():
        key_word = (''.join(choice(ascii_lowercase) for i in range(len(input_for_decrypt))))
    else:
        key_word = (''.join(choice(ascii_letters) for i in range(len(input_for_decrypt))))
    for i in range(len(input_for_decrypt)):
        char = input_for_decrypt[i]
        key_char = key_word[i % len(key_word)]
        decrypted += chr(ord(char) ^ ord(key_char))
    return decrypted, "\n\nGenerated keyword is: " + str(key_word)

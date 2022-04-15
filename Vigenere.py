from random import choice
from string import ascii_letters
from string import ascii_uppercase
from string import ascii_lowercase


def encrypt_by_vigenere_yourself(input_for_encrypt, key_word):  # encrypting by your own keyword
    encrypted = ""
    for i in range(len(input_for_encrypt)):
        char = input_for_encrypt[i]
        key_char = key_word[i % len(key_word)]
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            encrypted += char
        elif char.isupper():
            encrypted += chr((ord(char) - 65 + ord(key_char.upper()) - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) - 97 + ord(key_char.lower()) - 97) % 26 + 97)
    return encrypted


def encrypt_by_vigenere(input_for_encrypt):  # encrypting by generated keyword
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
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            encrypted += char
        elif char.isupper():
            encrypted += chr((ord(char) - 65 + ord(key_char.upper()) - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) - 97 + ord(key_char.lower()) - 97) % 26 + 97)
    return encrypted, "\n\nGenerated keyword is: " + str(key_word)


def decrypt_by_vigenere_yourself(input_for_decrypt, key_word):  # decrypting by known keyword
    decrypted = ""
    for i in range(len(input_for_decrypt)):
        char = input_for_decrypt[i]
        key_char = key_word[i % len(key_word)]
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            decrypted += char
        elif char.isupper():
            decrypted += chr((ord(char) - ord(key_char.upper())) % 26 + 65)
        else:
            decrypted += chr((ord(char) - ord(key_char.lower())) % 26 + 97)
    return decrypted


def decrypt_by_vigenere(input_for_decrypt):  # decrypting by generated keyword
    maybe_decrypted = ""
    if input_for_decrypt.isupper():
        key_word = (''.join(choice(ascii_uppercase) for i in range(len(input_for_decrypt))))
    elif input_for_decrypt.islower():
        key_word = (''.join(choice(ascii_lowercase) for i in range(len(input_for_decrypt))))
    else:
        key_word = (''.join(choice(ascii_letters) for i in range(len(input_for_decrypt))))
    for i in range(len(input_for_decrypt)):
        char = input_for_decrypt[i]
        key_char = key_word[i % len(key_word)]
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            maybe_decrypted += char
        elif char.isupper():
            maybe_decrypted += chr((ord(char) - ord(key_char.upper())) % 26 + 65)
        else:
            maybe_decrypted += chr((ord(char) - ord(key_char.lower())) % 26 + 97)
    return maybe_decrypted, "\n\nGenerated keyword is: " + str(key_word)

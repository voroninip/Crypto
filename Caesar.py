import random


def encrypt_by_caesar_yourself(input_for_encrypt, your_shift):  # encrypting by your own shift
    encrypted = ""
    for char in input_for_encrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            encrypted += char
        elif char.isupper():
            encrypted += chr((ord(char) + your_shift - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) + your_shift - 97) % 26 + 97)
    return encrypted


def encrypt_by_caesar(input_for_encrypt):  # encrypting by generated shift
    encrypted = ""
    generated_shift = int(random.uniform(1, 26))
    for i in range(len(input_for_encrypt)):
        char = input_for_encrypt[i]
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            encrypted += char
        elif char.isupper():
            encrypted += chr((ord(char) + generated_shift - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) + generated_shift - 97) % 26 + 97)
    return encrypted, "generated shift is: " + str(generated_shift)  # returns encrypted text and generated key


def decrypt_by_caesar_yourself(input_for_decrypt, encrypting_shift):  # decrypting by known shift
    decrypted = ""
    for char in input_for_decrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            decrypted += char
        elif char.isupper():
            decrypted += chr((ord(char) - encrypting_shift - 65) % 26 + 65)
        else:
            decrypted += chr((ord(char) - encrypting_shift - 97) % 26 + 97)
    return decrypted


def frequency_analysis_for_caesar(text_for_decrypt):  # decrypting by generated shift in way of frequency analysis
    maybe_encrypted = ""
    frequency = [0] * 26
    for char in text_for_decrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            pass
        elif char.isupper():
            frequency[ord(char) - 65] += 1
        else:
            frequency[ord(char) - 97] += 1

    most_frequent = 0
    for i in range(26):
        if frequency[i] == max(frequency):
            most_frequent = i
            break
    determined_shift = most_frequent + 65 - ord('E')

    for i in range(len(text_for_decrypt)):
        char = text_for_decrypt[i]
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            maybe_encrypted += char
        elif char.isupper():
            maybe_encrypted += chr((ord(char) - determined_shift - 65) % 26 + 65)
        else:
            maybe_encrypted += chr((ord(char) - determined_shift - 97) % 26 + 97)
    return maybe_encrypted

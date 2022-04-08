def encrypt_by_rot13(input_for_encrypt):
    encrypted = ""
    for char in input_for_encrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            encrypted += char
        elif char.isupper():
            encrypted += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            encrypted += chr((ord(char) + 13 - 97) % 26 + 97)
    return encrypted


def decrypt_by_rot13(input_for_decrypt):
    decrypted = ""
    for char in input_for_decrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            decrypted += char
        elif char.isupper():
            decrypted += chr((ord(char) - 13 - 65) % 26 + 65)
        else:
            decrypted += chr((ord(char) - 13 - 97) % 26 + 97)
    return decrypted

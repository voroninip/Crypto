def encrypt_by_atbash(input_for_encrypt):
    encrypted = ""
    for char in input_for_encrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            encrypted += char
        elif char.isupper():
            encrypted += chr(155 - ord(char))
        else:
            encrypted += chr(219 - ord(char))
    return encrypted


def decrypt_by_atbash(input_for_decrypt):
    decrypted = ""
    for char in input_for_decrypt:
        if ord(char) < 65 or ord(char) in range(91, 97) or 122 < ord(char):
            decrypted += char
        elif char.isupper():
            decrypted += chr(155 - ord(char))
        else:
            decrypted += chr(219 - ord(char))
    return decrypted

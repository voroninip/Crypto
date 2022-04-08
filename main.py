import argparse

import Caesar
import ROT13
import Atbash
import Vigenere
import Vernam

parser = argparse.ArgumentParser(description="Encryptor at your service...")
parser.add_argument("--in", dest="input_file", required=True,
                    help="File to work with.")
parser.add_argument("--task", required=True, choices=["encrypt", "decrypt"], type=str,
                    help="What do you want to do with file's text?")
parser.add_argument("--cipher", required=True, choices=["Caesar", "ROT13", "Atbash", "Vernam", "Vigener"], type=str,
                    help="What cipher do you want to operate with?")
parser.add_argument("--key",
                    help="The key (or shift) for the cipher.")
parser.add_argument("--out", dest="output_file", required=True,
                    help="Destination file to paste result.")

args = parser.parse_args()
input_file = args.input_file
task = args.task
cipher = args.cipher
key = args.key
output_file = args.output_file
file_for_reading = open(input_file, "r")
input_text = file_for_reading.read()
file_for_reading.close()
output_text = ""

def write_text(output_text):
    file_for_writing = open(output_file, "w")
    file_for_writing.write(output_text)
    file_for_writing.close()


def write_text_and_generated_key(output_text, generated_key_message):
    file_for_writing = open(output_file, "w")
    file_for_writing.write(output_text + generated_key_message)
    file_for_writing.close()


if task == "encrypt":
    if cipher == "Caesar":
        if key is None:
            output_text, generated_key_message = Caesar.encrypt_by_caesar(input_text)
            write_text_and_generated_key(output_text, generated_key_message)
        elif not isinstance(key, int):
            print("The key for Caesar cipher is shift: integer value from 1 to 25."
                  " Please enter an integer value for key.")
        else:
            output_text = Caesar.encrypt_by_caesar_yourself(input_text, key)
            write_text(output_text)
    elif cipher == "ROT13":
        if key is None:
            output_text = ROT13.encrypt_by_rot13(input_text)
            write_text(output_text)
        else:
            print("Can not be specified key for ROT13.")
    elif cipher == "Atbash":
        if key is None:
            output_text = Atbash.encrypt_by_atbash(input_text)
            write_text(output_text)
        else:
            print("Can not be specified key for Atbash.")
    elif cipher == "Vigener":
        if key is None:
            output_text, generated_key_message = Vigenere.encrypt_by_vigenere(input_text)
            write_text_and_generated_key(output_text, generated_key_message)
        elif not isinstance(key, str):
            print("The key for Vigener cipher has str type. Please enter a string for key.")
        else:
            output_text = Vigenere.encrypt_by_vigenere_yourself(input_text, key)
            write_text(output_text)
    elif cipher == "Vernam":
        if key is None:
            output_text, generated_key_message = Vernam.encrypt_by_vernam(input_text)
            write_text_and_generated_key(output_text, generated_key_message)
        elif not isinstance(key, str):
            print("The key for Vernam cipher has str type. Please enter a string for key.")
        else:
            output_text = Vernam.encrypt_by_vernam_yourself(input_text, key)
            write_text(output_text)
else:
    if cipher == "Caesar":
        if key is None:
            output_text = Caesar.frequency_analysis_for_caesar(input_text)
            write_text(output_text)
        elif not isinstance(key, int):
            print("The key for Caesar cipher is shift: integer value from 1 to 25."
                  " Please enter an integer value for key.")
        else:
            output_text = Caesar.decrypt_by_caesar_yourself(input_text, key)
            write_text(output_text)
    elif cipher == "ROT13":
        if key is None or int(key) == 13:
            output_text = ROT13.decrypt_by_rot13(input_text)
            write_text(output_text)
        else:
            print("Can not be specified key, except 13, for ROT13.")
    elif cipher == "Atbash":
        if key is None:
            output_text = Atbash.decrypt_by_atbash(input_text)
            write_text(output_text)
        else:
            print("Can not be specified key for Atbash.")
    elif cipher == "Vigener":
        if key is None:
            output_text, generated_key_message = Vigenere.decrypt_by_vigenere(input_text)
            write_text_and_generated_key(output_text, generated_key_message)
        elif not isinstance(key, str):
            print("The key for Vigener cipher has str type. Please enter a string for key.")
        else:
            output_text = Vigenere.decrypt_by_vigenere_yourself(input_text, key)
            write_text(output_text)
    elif cipher == "Vernam":
        if key is None:
            output_text, generated_key_message = Vernam.decrypt_by_vernam(input_text)
            write_text_and_generated_key(output_text, generated_key_message)
        elif not isinstance(key, str):
            print("The key for Vernam cipher has str type. Please enter a string for key.")
        else:
            output_text = Vernam.decrypt_by_vernam_yourself(input_text, key)
            write_text(output_text)

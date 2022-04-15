import argparse

import Caesar
import ROT13
import Atbash
import Vigenere
import Vernam

parser = argparse.ArgumentParser(description="Encryptor at your service...")
parser.add_argument("--in", dest="input_file", required=True,
                    help="File to work with.")
parser.add_argument("--task", dest="task", required=True, choices=["encrypt", "decrypt"], type=str,
                    help="What do you want to do with file's text? To encrypt or to decrypt?")
parser.add_argument("--cipher", dest="cipher", required=True,
                    choices=["Caesar", "ROT13", "Atbash", "Vernam", "Vigenere"], type=str,
                    help="What cipher do you want to operate with?")
parser.add_argument("--keyword", dest="keyword", required=False, type=str,
                    help="The keyword for the Vigenere or Vernam cipher.")
parser.add_argument("--shift", dest="shift", required=False, type=int,
                    help="The shift for the Caesar cipher. An integer value from 1 to 25.")
parser.add_argument("--out", dest="output_file", required=True,
                    help="Destination file to paste result.")

args = parser.parse_args()
input_file = args.input_file
task = args.task
cipher = args.cipher
keyword = args.keyword
shift = args.shift
output_file = args.output_file
file_for_reading = open(input_file, "r")
input_text = file_for_reading.read()
file_for_reading.close()
output_text = ""


def write_text(output_text):  # function of writing result to the output_file
    file_for_writing = open(output_file, "w")
    file_for_writing.write(output_text)
    file_for_writing.close()


def write_text_and_generated_key(output_text, generated_key_message):
    file_for_writing = open(output_file, "w")
    file_for_writing.write(output_text + generated_key_message)
    file_for_writing.close()


if task == "encrypt":
    if cipher == "Caesar":
        if keyword is None:
            if shift is None:
                output_text, generated_shift_message = Caesar.encrypt_by_caesar(input_text)
                write_text_and_generated_key(output_text, generated_shift_message)
            else:
                output_text = Caesar.encrypt_by_caesar_yourself(input_text, shift)
                write_text(output_text)
        else:
            print("Can not be specified keyword for Caesar, just only shift.")
    elif cipher == "ROT13":
        if keyword is None and shift is None:
            output_text = ROT13.encrypt_by_rot13(input_text)
            write_text(output_text)
        else:
            print("Can not be specified parameters for ROT13.")
    elif cipher == "Atbash":
        if keyword is None and shift is None:
            output_text = Atbash.encrypt_by_atbash(input_text)
            write_text(output_text)
        else:
            print("Can not be specified parameters for Atbash.")
    elif cipher == "Vigenere":
        if shift is None:
            if keyword is None:
                output_text, generated_keyword_message = Vigenere.encrypt_by_vigenere(input_text)
                write_text_and_generated_key(output_text, generated_keyword_message)
            else:
                output_text = Vigenere.encrypt_by_vigenere_yourself(input_text, keyword)
                write_text(output_text)
        else:
            print("Can not be specified shift for Vigenere, just only the keyword.")
    elif cipher == "Vernam":
        if shift is None:
            if keyword is None:
                output_text, generated_keyword_message = Vernam.encrypt_by_vernam(input_text)
                write_text_and_generated_key(output_text, generated_keyword_message)
            else:
                output_text = Vernam.encrypt_by_vernam_yourself(input_text, keyword)
                write_text(output_text)
        else:
            print("Can not be specified shift for Vernam, just only the keyword.")
else:  # task=="decrypt"
    if cipher == "Caesar":
        if keyword is None:
            if shift is None:
                output_text, generated_shift_message = Caesar.frequency_analysis_for_caesar(input_text)
                write_text_and_generated_key(output_text, generated_shift_message)
            else:
                output_text = Caesar.decrypt_by_caesar_yourself(input_text, shift)
                write_text(output_text)
        else:
            print("Can not be specified keyword for Caesar, just only shift.")
    elif cipher == "ROT13":
        if keyword is None and shift is None:
            output_text = ROT13.decrypt_by_rot13(input_text)
            write_text(output_text)
        else:
            print("Can not be specified parameters for ROT13.")
    elif cipher == "Atbash":
        if keyword is None and shift is None:
            output_text = Atbash.decrypt_by_atbash(input_text)
            write_text(output_text)
        else:
            print("Can not be specified parameters for Atbash.")
    elif cipher == "Vigenere":
        if shift is None:
            if keyword is None:
                output_text, generated_keyword_message = Vigenere.decrypt_by_vigenere(input_text)
                write_text_and_generated_key(output_text, generated_keyword_message)
            else:
                output_text = Vigenere.decrypt_by_vigenere_yourself(input_text, keyword)
                write_text(output_text)
        else:
            print("Can not be specified shift for Vigenere, just only the keyword.")
    elif cipher == "Vernam":
        if shift is None:
            if keyword is None:
                output_text, generated_keyword_message = Vernam.decrypt_by_vernam(input_text)
                write_text_and_generated_key(output_text, generated_keyword_message)
            else:
                output_text = Vernam.decrypt_by_vernam_yourself(input_text, keyword)
                write_text(output_text)
        else:
            print("Can not be specified shift for Vernam, just only the keyword.")

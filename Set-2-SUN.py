def shift_letter(letter, shift):
    if letter == " ":
        return " "
    else:
        base_ascii = ord("A")
        shifted_ascii = (ord(letter) - base_ascii + shift) % 26 + base_ascii
        return chr(shifted_ascii)

def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isspace():
            result += " "
        else:
            result += shift_letter(char, shift)
    return result

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "
    else:
        base_ascii = ord("A")
        shift_value = ord(letter_shift) - base_ascii
        shifted_ascii = (ord(letter) - base_ascii + shift_value) % 26 + base_ascii
        return chr(shifted_ascii)
        
def vigenere_cipher(message, key):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    key_index = 0
    for char in message:
        if char.upper() in alphabet:
            message_index = alphabet.index(char.upper())
            key_char = key[key_index % len(key)].upper()
            key_index_value = alphabet.index(key_char)
            shifted_index = (message_index + key_index_value) % 26
            result += alphabet[shifted_index]
            key_index += 1
        else:
            result += char
            key_index += 1
    return result

def scytale_cipher(message, shift):
    num_rows = (len(message) + shift - 1) // shift
    if len(message) % shift != 0:
        message += "_" * (num_rows * shift - len(message))
    encoded_message = ""
    for i in range(len(message)):
        encoded_message += message[(i // shift) + (len(message) // shift) * (i % shift)]
    return encoded_message

def scytale_decipher(message, shift):
    return ''.join([message[i::shift] for i in range(shift)])


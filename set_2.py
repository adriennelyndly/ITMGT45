def shift_letter(letter, shift):
    if letter == " ":
        return " "

    position = ord(letter) - ord("A")
    new_position = (position + shift) % 26
    return chr(new_position + ord("A"))

def caesar_cipher(message, shift):
    result = ""
    for character in message: 

        if character == " ":
            result += " "

        else:
            position = ord(character) - ord("A")
            new_position = (position + shift) % 26
            result += chr(new_position + ord("A"))

    return result 

def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return " "

    shift_value = ord(letter_shift) - ord("A")
    position = ord(letter) - ord("A")
    new_position = (position + shift_value) % 26

    return chr(new_position + ord("A"))

def vigenere_cipher(message, key):
    result = ""
    key_length = len(key)
    key_index = 0

    for character in message:
        key_letter = key[key_index % key_length]
        shift_amount = ord(key_letter) - ord("A")

        if character == " ":
            result += " "

        else: 
            position = ord(character) - ord("A")
            new_position = (position + shift_amount) % 26
            result += chr(new_position + ord("A"))

        key_index += 1

    return result
    
def scytale_cipher(message, shift):
    while len(message) % shift != 0:
        message += "_"
    
    n = len(message)      
    rows = n // shift     

    encoded = ""
    for i in range(n):
        index = (i // shift) + rows * (i % shift)
        encoded += message[index]
    
    return encoded

def scytale_decipher(message, shift):
    n = len(message)
    rows = n // shift 

    decoded = ""
    for x in range(n):
        a = x % rows
        b = x // rows 
        i = a * shift + b 
        decoded += message[i]
    
    return decoded 
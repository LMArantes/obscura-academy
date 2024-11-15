# Caesar Code
def caesar_encode(text, shift):
    encoded_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            encoded_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encoded_text += char
    return encoded_text


def caesar_decode(text, shift):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            decoded_text += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decoded_text += char
    return decoded_text


# Vigerene Cipher
def vigenere_encode(plaintext, keyword):
    encoded_text = ""
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    keyword_length = len(keyword)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            offset = 65
            shift = ord(keyword[i % keyword_length]) - 65
            encoded_text += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            encoded_text += char

    return encoded_text


def vigenere_decode(ciphertext, keyword):
    decoded_text = ""
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    keyword_length = len(keyword)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            offset = 65
            shift = ord(keyword[i % keyword_length]) - 65
            decoded_text += chr((ord(char) - offset - shift) % 26 + offset)
        else:
            decoded_text += char

    return decoded_text


# Atbash
def atbash_cipher(text):
    transformed_text = ""
    for char in text.upper():
        if char.isalpha():
            offset = 65
            transformed_text += chr(25 - (ord(char) - offset) + offset)
        else:
            transformed_text += char
    return transformed_text

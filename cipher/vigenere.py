from cipher.romanian_alphabet import romanian_alphabet, reversed_romanian_alphabet, romanian_alphabet_length


def vigenere_encryption(message, key):
    encrypted_message = ''
    key_letter_index = 0

    for char in message:
        if char not in romanian_alphabet:
            encrypted_message += char
        else:
            message_codification = romanian_alphabet[char]
            key_codification = romanian_alphabet[key[key_letter_index]]
            encrypted_message += reversed_romanian_alphabet[(message_codification + key_codification) % romanian_alphabet_length]

            if key_letter_index == len(key) - 1:
                key_letter_index = 0
            else:
                key_letter_index += 1

    return encrypted_message


def vigenere_decryption(message, key):
    decrypted_message = ''
    key_letter_index = 0

    for char in message:
        if char not in romanian_alphabet:
            decrypted_message += char
        else:
            message_codification = romanian_alphabet[char]
            key_codification = romanian_alphabet[key[key_letter_index]]
            decrypted_message += reversed_romanian_alphabet[(message_codification - key_codification) % romanian_alphabet_length]

            if key_letter_index == len(key) - 1:
                key_letter_index = 0
            else:
                key_letter_index += 1

    return decrypted_message

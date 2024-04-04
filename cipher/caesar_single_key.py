from cipher.alphabet import alphabet, reversed_alphabet


def caesar_single_key_encryption(message, key, dictionary=alphabet, reversed_dictionary=reversed_alphabet):
    encrypted_message = ''

    for char in message:
        if char not in dictionary:
            encrypted_message += char
            continue
        else:
            encrypted_index = (dictionary[char] + key) % 26
            encrypted_message += reversed_dictionary[encrypted_index]

    return encrypted_message


def caesar_single_key_decryption(encrypted_message, key, dictionary=alphabet, reversed_dictionary=reversed_alphabet):
    decrypted_message = ''

    for char in encrypted_message:
        if char not in dictionary:
            decrypted_message += char
            continue
        else:
            decrypted_index = (dictionary[char] - key) % 26
            decrypted_message += reversed_dictionary[decrypted_index]

    return decrypted_message

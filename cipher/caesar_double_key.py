from cipher.alphabet import reversed_alphabet
from cipher.caesar_single_key import caesar_single_key_encryption, caesar_single_key_decryption


def caesar_double_key_encryption(message, int_key, string_key):
    dictionary = create_dictionary(string_key)
    reversed_dictionary = create_reversed_dictionary(dictionary)

    return caesar_single_key_encryption(message, int_key, dictionary, reversed_dictionary)


def create_dictionary(string_key):
    dictionary = {}
    index = 0

    for char in string_key:
        if char not in dictionary:
            dictionary[char] = index
            index += 1

    for i in range(0, 26):
        if reversed_alphabet[i] not in dictionary:
            dictionary[reversed_alphabet[i]] = index
            index += 1

    return dictionary


def create_reversed_dictionary(dictionary):
    return {v: k for k, v in dictionary.items()}


def caesar_double_key_decryption(message, int_key, string_key):
    dictionary = create_dictionary(string_key)
    reversed_dictionary = create_reversed_dictionary(dictionary)

    return caesar_single_key_decryption(message, int_key, dictionary, reversed_dictionary)

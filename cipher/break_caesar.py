from collections import Counter
from cipher.wordlist import wordlist
from cipher.alphabet import alphabet, reversed_alphabet
from cipher.letter_frequency import letter_frequency
from cipher.caesar_double_key import create_dictionary, create_reversed_dictionary


def caesar_shift(text, shift, used_alphabet, used_reversed_alphabet):
    shifted_text = ""
    for char in text:
        if char in used_alphabet:
            new_index = (used_alphabet[char] + shift) % 26
            shifted_text += used_reversed_alphabet[new_index]
        else:
            shifted_text += char

    return shifted_text


def frequency_analysis(ciphertext, used_alphabet, used_reversed_alphabet):
    frequencies = Counter(c for c in ciphertext if c.isalpha())
    best_shift = 0
    min_difference = float('inf')

    for shift in range(26):
        total_difference = 0

        for letter, freq in frequencies.items():
            shifted_index = (used_alphabet[letter] + shift) % 26
            shifted_letter = used_reversed_alphabet[shifted_index]
            expected_freq = letter_frequency.get(shifted_letter, 0)
            total_difference += abs(freq - expected_freq)

        if total_difference < min_difference:
            min_difference = total_difference
            best_shift = shift

    return -best_shift


def word_analysis(ciphertext, used_alphabet, used_reversed_alphabet):
    best_shift = 0
    max_words = 0
    for shift in range(26):
        decrypted_text = caesar_shift(ciphertext, shift, used_alphabet, used_reversed_alphabet).lower().split()
        common_words = sum(word in wordlist for word in decrypted_text)
        if common_words > max_words:
            max_words = common_words
            best_shift = shift
    return best_shift


def decrypt_caesar(ciphertext, string_key=None):

    if string_key is not None:
        used_alphabet = create_dictionary(string_key)
        used_reversed_alphabet = create_reversed_dictionary(used_alphabet)
    else:
        used_alphabet = alphabet
        used_reversed_alphabet = reversed_alphabet

    initial_shift = frequency_analysis(ciphertext, used_alphabet, reversed_alphabet)
    decrypted_with_initial_shift = caesar_shift(ciphertext, initial_shift, used_alphabet, used_reversed_alphabet)
    final_shift = word_analysis(decrypted_with_initial_shift, used_alphabet, used_reversed_alphabet)
    decrypted_text = caesar_shift(decrypted_with_initial_shift, final_shift, used_alphabet, used_reversed_alphabet)

    shifted_alphabet = {char: used_reversed_alphabet[(index + final_shift + initial_shift) % 26] for char, index in used_alphabet.items()}

    return decrypted_text, shifted_alphabet

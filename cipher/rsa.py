import gmpy2
from gmpy2 import gcd


def check_p_q(num1, num2):
    return gmpy2.is_prime(num1) and gmpy2.is_prime(num2)


def generate_n(p, q):
    return p * q


def generate_euler_indicator(p, q):
    return (p - 1) * (q - 1)


def validate_e(e, euler_indicator):
    return gcd(e, euler_indicator) == 1 and 1 < e < euler_indicator


def modular_exponentiation(a, b, n):
    result = 1
    base = a % n

    while b > 0:
        if b % 2 == 1:
            result = (result * base) % n

        base = (base * base) % n

        b //= 2

    return result


def extended_gcd(a, b):
    old_r, r = a, b
    old_y, y = 1, 0

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_y, y = y, old_y - quotient * y

    return old_r, old_y


def mod_inverse(e, euler_indicator):
    res, y = extended_gcd(e, euler_indicator)
    if res != 1:
        return -1
    else:
        return y % euler_indicator


def encrypt_character(m, e, n):
    ascii_value = ord(m)
    return modular_exponentiation(ascii_value, e, n)


def decrypt_character(c, d, n):
    decrypted_ascii = modular_exponentiation(c, d, n)
    return chr(decrypted_ascii)

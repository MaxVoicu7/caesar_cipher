def is_valid_key(key):
    try:
        key = int(key)

        if key < 1 or key > 25:
            return False

        return True

    except ValueError:
        return False


def string_to_int_list(input_string):
    string_list = input_string.split()
    int_list = [int(num) for num in string_list]

    return int_list

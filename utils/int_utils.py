def is_valid_key(key):
    try:
        key = int(key)

        if key < 1 or key > 25:
            return False

        return True

    except ValueError:
        return False

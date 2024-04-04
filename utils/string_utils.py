def is_valid_string_key(message):
    if not message:
        return False

    return all(char.isalpha() for char in message)


def get_validated_message(message):
    return message.upper()

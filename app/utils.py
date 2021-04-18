import string


def b62_encode(number):
    base = string.digits + string.ascii_letters

    if number == 0:
        return "0"

    base62 = []
    while number != 0:
        number, i = divmod(number, 62)
        base62.append(base[i])

    return ''.join(reversed(base62))

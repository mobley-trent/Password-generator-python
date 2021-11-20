def password_generator(length):
    '''
    A simple password generator that takes length as the only requirement.
    Returns a random password with uppercase, lowercase and special characters.
    '''

    import random
    from re import search
    import string

    chars = string.ascii_letters + string.digits + '!@£$%&?'

    gen_pass = ''.join([random.choice(chars) for n in range(length)])
    regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[!@£$%&?])[A-Za-z0-9!@£$%&?]{6,}$"
    valid = bool(search(regex, gen_pass))

    while not valid:
        gen_pass = ''.join([random.choice(chars) for n in range(length)])
        valid = bool(search(regex, gen_pass))

    return gen_pass



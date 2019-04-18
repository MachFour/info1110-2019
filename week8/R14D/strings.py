def get_first_lowercase_pair(text):
    """Return the index of the first pair of letters that are both
    lowercase in the given string. If no such pair exists, return -1.
    """
    #if type(text) == str:
    if not isinstance(text, str):
        return -1

    # text = 'AhAhAhAhA'
    i = 0
    while i < len(text):
        a = text[i]
        if a.islower():
            b = text[i+1]
            if b.islower():
                return i
        i += 1

    return -1

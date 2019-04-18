digits = '0123456789'

# take a string of length 1 and try to convert it into a digit
# if it's not possible, raise a ValueError
def digit_to_int(s):
    if not isinstance(s, str) or len(s) != 1:
        raise ValueError("Not a digit")
    # now, s is a string of length 1
    #i = digits.find(s)
    i = 0
    while i < len(digits):
        # manually checks if s is equal to any digit
        if digits[i] == s:
            return i
        i += 1
    raise ValueError("Not a digit")

def string_to_int(s):
    # how should it work for one digit?
    # how should it work if s is not a string?
    # how should it work for an empty string?

    if not isinstance(s, str):
        return None
    elif len(s) == 0:
        return None

    number = 0
    index = 0
    rightmost_index = len(s) - 1
    try:
        while index < len(s):
            # digit is an int already
            digit = digit_to_int(s[rightmost_index - index])
            number += digit*(10**index) # posititional arithmetic
            index += 1
        return number
    except ValueError:
        return None


    #if s >= 0:
    #    if s < 10:
    #else:
    #    raise Exception("I'm not finished yet!")

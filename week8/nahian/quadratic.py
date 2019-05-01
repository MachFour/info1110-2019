import math

def quadratic(a, b, c):
    if (type(a) != int or
        type(b) != int or
        type(c) != int):
        # Arguments have incorrect type
        raise TypeError('arguments must have type `int`')

    if a == 0:
        raise ValueError('coefficient `a` cannot be zero')

    disc = b**2 - 4*a*c             # the discriminant

    if disc < 0:
        return ()                   # return an empty tuple
    if disc == 0:
        return -b / (2*a),          # return a tuple with one element
    else:
        sq_dc = math.sqrt(disc)
        return (
            (-b+sq_dc) / (2*a),
            (-b-sq_dc) / (2*a)
        )                           # return a tuple with two elements


if __name__ == '__main__':
    # The code inside this `if` block executes only if this
    # program is run in the Terminal.
    #
    # This code won't be executed if it was imported by
    # another program.

    # Get the values of coefficients `a`, `b` and `c`
    NAMES = ['a', 'b', 'c']
    coeffs = []

    i = 0
    while i <= 2:
        var = NAMES[i]
        num = input('Enter {}: '.format(var))
        try:
            num = int(num)
        except ValueError:
            continue

        coeffs.append(num)
        i += 1

    a, b, c = coeffs  # unpack the list of coefficients
    print()
    print('The equation {}x^2 + {}x + {} = 0 has solutions:'.format(a, b, c))

    solns = quadratic(a, b, c)
    if len(solns) == 0:
        print('There are no real solutions!')
    elif len(solns) == 1:
        x = solns[0]
        print('x={:.2f}'.format(x))
    else:
        x_1, x_2 = solns  # unpack the tuple of solutions
        print('x={:.2f}, x={:.2f}'.format(x_1, x_2))

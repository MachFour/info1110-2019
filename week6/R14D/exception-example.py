def divide(a, b):
    if b == 0:
        # Question: why might we want to do this?
        # What happens if we don't give ZeroDivisionError() any arguments?
        raise ZeroDivisionError('A helpful message!')
    return a / b

a = input('Numerator: ')
b = input('Denominator: ')

try:
    x = int(a)
    y = int(b)
    n = divide(x, y)
    print('Result: {}'.format(n))
except ZeroDivisionError as e:
    print(e) # Why do we use the 'as' keyword here?
except ValueError:
    print('What happened?')
except Exception:
    print('Will I ever trigger?')
finally:
    print('I always have the last laugh :D')

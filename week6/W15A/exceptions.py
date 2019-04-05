def divide(a,b):
    if not a.isdigit() or not b.isdigit():
        raise ValueError("a or b is not a digit.")

    if float(b) == 0:
        # Throw an error
        raise ZeroDivisionError("Zero division error: value of a: {} and value of b: {}".format(a,b))
    return float(a)/float(b)

while True:

    a = input("Numerator: ")
    b = input("Denominator: ")

    # Try block
    try:
        divide(a,b)
    # Catch block 
    except ZeroDivisionError as err:
        print("Caught a ZeroDivsion error")
        print(err)
        raise RuntimeError("The user is very dumb.") 
    except ValueError as err:
        print("Caught a Value error")
        print(err)
    finally: # Doing any cleanup work
        print("Please type in more numbers")

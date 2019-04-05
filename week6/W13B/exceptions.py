def divide(a, b):
    if not a.isdigit() or not b.isdigit():
        raise ValueError("a or b are not numbers.")

    if float(b) == 0:
        # IF my b is equal to 0
        # Raise a more meaningful exception
        raise ZeroDivisionError("Zero Division Error: Value of a was {} and value of b was {}".format(a,b))
    
    return float(a)/float(b)

while True:
    a = input("Numerator: ")
    b = input("Denominator: ")


    try:
        x = divide(a,b)
    except ZeroDivisionError as err:
        print("Catching Zero Divsion Error \n {}".format(err))
        raise Exception("The user is dumb")
    except ValueError as err:
        print("Catching Value Error \n {}".format(err))
        continue
    finally:
        print("Try putting in different numbers again")

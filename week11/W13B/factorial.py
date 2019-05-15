
def factorial(n):
    if n < 0:
        raise ValueError("n can't be negative!")
    # base case:
    elif n == 0 or n == 1:
        return 1
    # recursive case
    # (don't need else)
    return n*factorial(n-1)

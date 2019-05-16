def factorial(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        # base case - not recursive
        return 1
    else: # n > 0
        # recursive case
        return n * factorial(n-1)

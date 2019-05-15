def factorial(n):
    if n < 0:
        raise ValueError("n should be >= 0")
    # base case
    if n == 0:
        return 1
    else:
        # recursive
        return n * factorial(n-1)

def binomial(n, k):
    if n < 0 or k < 0:
        raise ValueError("n and k must be >= 0")
    elif n - k < 0:
        raise ValueError("k cannot be larger than n")
    # know result will be an integer anyway, so floor division is ok
    return factorial(n)//(factorial(k)*factorial(n-k))


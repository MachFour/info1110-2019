def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    print("fibonacci({:d})".format(n))
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # recursive formula:
        # F(n) = F(n-1) + F(n-2)
        return fibonacci(n-1) + fibonacci(n-2)



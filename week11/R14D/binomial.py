from factorial import factorial
# from <file.py> import <function>
def binomial(n, k):
    if n < 0 or k < 0:
        raise ValueError("n and k must be >= 0")
    elif n - k < 0:
        raise ValueError("k cannot be larger than n")
    # know result will be an integer anyway, so floor division is ok
    return factorial(n)//(factorial(k)*factorial(n-k))

def binomial2(n, k):
    if n < 0 or k < 0:
        raise ValueError("n and k must be >= 0")
    elif n - k < 0:
        raise ValueError("k cannot be larger than n")
    print("binomial2({:d}, {:d})".format(n, k))
    # base cases:
    if k == 0 or n == k:
        return 1
    else:
        return binomial2(n-1, k-1) + binomial2(n-1, k)

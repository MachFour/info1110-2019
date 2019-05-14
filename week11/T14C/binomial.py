from factorial import factorial

def binomial(n, k):
    if n == 0 or k == 0:
        return 1

    return (factorial(n))/(factorial(k)*factorial(n-k))

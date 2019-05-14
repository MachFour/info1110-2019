def spam(n):
    if n == 0:
        return n
    result = spam(n-1)
    return result

ham = spam(3)
print(ham)

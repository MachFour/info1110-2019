def fibonacci(n):
    l = [0,1] # We know these are our base cases
    i = 2
    while i < n:
        value = l[i-1] + l[i-2]
        l.append(value)

        i += 1
    return l[-1] # -1 is the last element in the list





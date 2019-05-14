def hailstones(n, l=[]):
    l.append(n)
    if n == 1: # if n == 1 return the list
        return l
    if n%2 == 0:
        # If n is even
        n = n//2
    else:
        # If n is odd 
        n = n*3 + 1

    return hailstones(n, l)

print(hailstones(6, []))
print(hailstones(3, []))
print(hailstones(10, []))
print(hailstones(1, []))

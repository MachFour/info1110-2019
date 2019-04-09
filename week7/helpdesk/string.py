
l = ['a', True, 210.3]
# print out a string representation

def string(l):
    if l == []:
        return "[]"
    # else l has at least one element
    # we can do the first element manually
    s = '[' + str(l[0])
    i = 1
    while i < len(l):
        s += ', ' + str(i)
        i += 1
    s += ']'
    return s

print(string(l))

number = 6
def f1():
    # this variable hides the global one
    number = 7
    # the global number won't be changed
    print(number)

def f2():
    global number
    # now we can change the global 'number'
    number = 7
    print(number)

def f3():
    # 'number' refers to the global variable
    print(number)
    # trying to modify a global variable
    # will give an error
    number = 8

print(number)
f2()
print(number)

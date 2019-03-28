a = 123
if a == "123":
    print("a is 123")
    if a > 0:
        print("a is greater than 0")
else:
    print("a is less than or equal to 0???")

a = 123
while True:
    if a == 123:
        print("Hello from inside the while loop")
        a = a - 1
    elif a > 122 or a < 0:
        break
    else:
        a = a - 1
        print("here's an else")

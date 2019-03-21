i = int(input("Number: "))
even = i % 2 == 0
in_range = i >= 20 and i <= 200
odd = not even
negative = i < 0
test_pass = (even and in_range) or (odd and negative)
if test_pass:
    print("{:d} passes the test!\n".format(i))
else:
    print("{:d} fails the test :(\n".format(i))

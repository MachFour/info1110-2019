i = int(input("Number: "))
# check if i is even and in the range [20, 200] (inclusive),
# or i is odd and negative
if (i % 2 == 0 and i > 20 and i < 200) or (i % 2 == 1 and i < 0):
    print("{:d} passes the test!\n".format(i))
else:
    print("{:d} fails the test :(\n".format(i))

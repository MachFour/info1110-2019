number = int(input("Integer: "))

is_even = number%2 == 0
is_odd = not is_even
is_within_range = 20 <= number <= 200
is_negative = number < 0


if is_even and is_within_range:
    print("{} passes the test.".format(number))
# Else if number is odd and negative
elif is_odd and is_negative:
    print("{} passes the test.".format(number))
else:
    print("{} does not pass the test.".format(number))

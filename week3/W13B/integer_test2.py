num = int(input("Integer :"))

is_even = num%2 == 0
is_odd = not is_even
is_in_range = 20 <= num <= 200
is_negative = num < 0

if (is_even and is_in_range) or (is_odd and is_negative):
    print("{} passes the test!".format(num))
else:
    print("{} failed the test :(".format(num))

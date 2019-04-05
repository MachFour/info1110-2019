num = 1
line = ''

# num <= 100
while num <= 100:
    # num is odd
    if num%2 != 0:
        line += str(num) + ', '
    num = num + 1

print(line)

num = 1
line = ''

while num <= 100:
    # If num is odd
    if num%2 != 0:
        line += str(num) + ', '
    num += 1

print(line)

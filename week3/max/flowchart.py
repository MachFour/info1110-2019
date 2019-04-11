# flow chart exercise
num = 1
line = '1'

num = 2
while num <= 100:
    # check: num is odd?
    if num % 2 == 1:
        line += ", " + str(num)
    # this line below is always executed
    num += 1
# at the end

print(line)


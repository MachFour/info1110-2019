#
# Print out all triangular numbers that are:
# less than 15
# and either a multiple of 2 or 5
#

t_num = 1
step = 2
print('Hello!')

while True:
    if t_num >= 15:
        break

    if t_num % 2 == 0:
        print(t_num)
    elif t_num % 5 == 0:
        print(t_num)

    t_num += step
    step += 1


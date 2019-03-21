t_num = 1
step = 2
print('Hello!')

while t_num < 15:
    divisible_by_2 = t_num % 2 == 0
    divisible_by_5 = t_num % 5 == 0

    if divisible_by_2 or divisible_by_5:
        print(t_num)

    t_num += step
    step += 1

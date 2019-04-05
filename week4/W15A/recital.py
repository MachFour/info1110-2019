# Perfect for usage of strings

num_list = []

while True:
    num = float(input("Number: "))
    if num == 0:
        break
    else:
        num_list.append(num)


print("Your numbers were:")


# Iterate through the list to print all the members one by one
i = 0
while i < len(num_list):
    print("Number: {}".format(num_list[i]))
    i+=1

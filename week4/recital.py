# recital.py

number_list = [] # len(number_list) == 0

while True:
    number = float(input("Number: "))
    if number == 0:
        # don't add zero to the list
        break

    number_list.append(number)
print()
i = 0
while i < len(number_list):
    print(number_list[i])
    i += 1

# all done

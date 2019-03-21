import sys

check_for_8 = False
if len(sys.argv) >= 2 and sys.argv[1] == "-find8":
    check_for_8 = True

number_string = input("Enter some integers: ")
# example: number_string = "2, 3, 4, 5, 6"
# this is a list of strings, one for each number
separated_numbers = number_string.split(",")
# this will store the actual numbers
number_list = []
i = 0
while i < len(separated_numbers):
    number_list.append(int(separated_numbers[i]))
    i += 1

print("Your numbers were:", number_list)

if check_for_8:
    i = 0
    while i < len(number_list):
        if number_list[i] == 8:
            print("The number 8 is at index", i)
            break
        i += 1

# standard input -> input()
# (also sys.argv)

numbers = []
while True:
    number = float(input("Number: "))
    if number == 0:
        break
    numbers.append(number)

print()
print("Your numbers were: ")

i = 0
while i < len(numbers):
    print(numbers[i]) # item at index i
    i += 1


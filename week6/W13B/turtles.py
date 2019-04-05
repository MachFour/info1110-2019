names = []
ages = []

while True:
    turtle_input = input("Turtle data: ")
    # "Adam, 3" --> ["Adam", "3"]
    # Lucy, 4 --> ["Lucy", "4"]
    if turtle_input == "STOP":
        break
    turtle_input = turtle_input.split(", ")
    names.append(turtle_input[0])
    ages.append(turtle_input[1])

if(len(names) == 0):
    print("There are no turtles here!")

i = 0
while i < len(names):
    print("{} is {} year(s) old.".format(names[i], ages[i]))
    i+=1


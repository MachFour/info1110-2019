import sys

def read_turtle_data():
    turtles = []
    while True:
        next_data = input("Turtle data: ")
        if next_data == "STOP":
            break
        name_age = next_data.split(",")
        if len(name_age) != 2:
            raise ValueError("Name and age must be separated by a comma")
        try:
            name = name_age[0]
            age = int(name_age[1])
            turtle = (name, age)
            turtles.append(turtle)
        except ValueError:
            raise ValueError("Please make sure the age is an integer")
    return turtles

try:
    turtles = read_turtle_data()
except ValueError as e:
    print(e)
    sys.exit(1)

if len(turtles) == 0:
    print("There are no turtles here!")
    sys.exit(1)

index = 0
while index < len(turtles):
    turtle = turtles[index] # (name, age)
    print("{} is {} year(s) old.".format(turtle[0], turtle[1]))
    index += 1

#for turtle in turtles:
#    print("{} is {} year(s) old.".format(turtle[0], turtle[1]))



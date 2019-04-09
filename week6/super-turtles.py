# this will be a list of tuples: (name <str>, age <int>)
turtles = []

while True:
    next_data = input("Turtle data: ")
    if next_data == "STOP":
        break # go to end of loop

    data_strings = next_data.split(",") # separate into a list of strings

    if len(data_strings) != 2:
        print("Please use the format: <name>, <age>")
        continue # go to top of loop

    try:
        # strip() returns a copy of the string that has any
        # space/tab/newline characters at the beginning or end removed
        name = data_strings[0].strip()
        age = int(data_strings[1].strip())
        new_turtle = (name, age) # combine data into as tuple
        turtles.append(new_turtle)
    # catch error from int()
    except ValueError:
        print("-> Please enter age as an integer", end="\n\n")

if len(turtle_data) > 0:
    index = 0
    while index < len(turtle_data):
        next_turtle = turtles[i]
        print("{} is {} years old".format(next_turtle[0], next_turtle[1]))
        index += 1
    # for turtle in turtles:
else:
    print("There are no turtles here!")

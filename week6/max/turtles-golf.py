l = [[0]]
while l[-1][0] != "STOP":
    l.append(input("Turtle data: ").split(", "))
l = l[1:-1]
if not l: print("There are no turtles here!")
for t in l: print(t[0],"is",t[1],"years old")

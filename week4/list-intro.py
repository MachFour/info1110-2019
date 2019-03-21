
print("""
###############################################
### A quick introduction to lists in Python ###
###############################################
""")

print("We can define a new empty list l by writing:")
print("> l = []", end="\n\n")
l = []

print("After initialising l:")
print("l =", l, "and len(l) is", len(l), end="\n\n")

print("We can add items to the list with the append() function:")
print("> l.append(5)", end="\n\n")
l.append(5)

print("After appending 5:")
print("l =", l, "and len(l) is", len(l), end="\n\n")

print("In python, lists don't have to contain objects of the same type!")
print("> l.append('strawberry')", end="\n\n") # note the difference in quotes!
l.append('strawberry')

print("After appending 'strawberry':")
print("l =", l, "and len(l) is", len(l), end="\n\n")

print("The append() function always adds items to the end of the list,")
print("but the insert() function can add items anywhere.", end="\n\n")

print("Let's insert the number 10 at the start of the list (index 0)")
print("> l.insert(0, 10)", end="\n\n")
l.insert(0, 10)

print("After inserting 10:")
print("l =", l, "and len(l) is", len(l), end="\n\n")

print("We can access items of a list using square brackets [],")
print("just like with we did with sys.argv:")
print("> print(l[2])")
print(" ", l[2], end="\n\n")

print("What's new is that we can actually change the items of the list,")
print("using the square brackets on the left hand side of an equals sign:")
print("> l[2] = 8")
l[2] = 8

print("After this change:")
print("l =", l, "and len(l) is", len(l), end="\n\n")

print("In this way, a list is like a set of numbered variables", end="\n\n")

print("There are lots more things you can do with lists,")
print("for example printing out each element on a separate line:", end="\n\n")

i = 0
while i < len(l):
    print("The item at index {:d} is {}".format(i, l[i]))
    i += 1

print()
print("(See the code for how to do this)")
print()

print("Some more helpful list functions are found here:")
print("https://docs.python.org/3/tutorial/datastructures.html#data-structures")

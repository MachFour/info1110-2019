ls = []

# This loop always exits via the 'break' statement.
# Since len(ls) increases by 1 each time we use ls.append(),
# i < len(ls) was always True. So we can just put 'while True'
while True:
    t1 = input("")
    if t1 == "":
        break
    ls.append(t1)

i = 0 # print the strings with even index
while i < len(ls):
    print(ls[i])
    i += 2

print() # add a blank line to pass the test case

i = 1 # print the strings with odd index
while i < len(ls):
    print(ls[i])
    i += 2

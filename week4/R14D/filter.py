import sys
# read 2 arguments from sys.argv

if not len(sys.argv) >= 3:
    print("Please give a filename and a letter")
    sys.exit(1)

filename = sys.argv[1]
# treat the string sys.argv[2] as a list of characters,
# and get only the first one
letter = sys.argv[2][0]


#open a text file for reading
f = open(filename, "rt")

while True:
    line = f.readline()
    if line == "":
        # reached the end of the file
        break
    line_without_enter = line.rstrip("\n")
    # check if the first letter matches
    if line_without_enter[0] == letter:
        print(line_without_enter)

f.close()

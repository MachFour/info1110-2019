import sys
def readlines(path):
    # open file for reading
    f = open(path, "r")
    # list that will store all lines in the file
    lines = []
    while True:
        text_line = f.readline()
        if text_line == "": # end condition
            break
        stripped_line = text_line.strip()
        lines.append(stripped_line)
    return lines

try:
    path = sys.argv[1]
    lines = readlines(path)
    print(lines)
except FileNotFoundError:
    print("File was not found!")
except IndexError:
    print("Please give a filename")




def readlines(path):
    # this will store the lines in the file
    lines = []

    f = open(path, 'r')
    # reads until the next newline character
    while True:
        next_line = f.readline()
        if next_line == "":
            # end of file
            break
        # remove whitespace at the start and the end
        lines.append(next_line.strip())
    # always
    f.close()

    return lines

import sys

try:
    path = sys.argv[1]
    lines = readlines(path)
    print("The lines were")
    print(lines) # this is incomplete
except IndexError:
    print("Please enter a file path")

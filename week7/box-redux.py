def print_box(height):
    # assume that height is an integer
    if height <= 0:
        return # don't print anything
    width = 2*height
    row = 0
    while row < height:
        # print out the box characters, column by column
        column = 0
        while column < width:
            if row == 0 or row == height-1:
                if column == 0 or column == width - 1:
                    print("+", end='') # corners
                else:
                    print("-", end='') # top edges
            else:
                if column == 0 or column == width - 1:
                    print("|", end='') # sides
                else:
                    print(" ", end='') # middle
            column += 1
        # end of row
        row += 1
        print()

# command line arguments:
import sys

try:
    height = int(sys.argv[1])
    print_box(height)
except IndexError:
    print("Please specify a height for the box")
except ValueError:
    print("Height needs to be an int")



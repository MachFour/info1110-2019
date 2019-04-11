def which_character(row, column, height, width):
    if row == 0 or row == height-1:
        if column == 0 or column == width - 1:
            return "+" # corners
        else:
            return "-" # top edges
    else:
        if column == 0 or column == width - 1:
            return "|" # sides
        else:
            return " " # middle

def print_box(height):
    # assume that height is an integer
    if height <= 0:
        raise ValueError("Height must be positive")
    width = 2*height
    row = 0
    while row < height:
        # print out the box characters, column by column
        column = 0
        while column < width:
            # decide which character to print
            c = which_character(row, column, height, width)
            print(c, end = '')
            column += 1
        # end of row
        row += 1
        print()

if __name__ == "__main__":
    import sys
    try:
        # command line arguments:
        height = int(sys.argv[1])
        print_box(height)
    except IndexError:
        print("Please specify a height for the box")
    except ValueError:
        print("Height needs to be an int")



import sys

def print_box(height):
    # Calculate width
    width = 2*height
    row = 0
    
    # Iterate from first row to last row
    while row < height:
        to_print = ''
        if row == 0 or row == height-1:
            first_and_last = '+'
            middle_character = '-'
        else:
            first_and_last = '|'
            middle_character = ' '

        column = 0
        
        # Iterate from first column to last column
        while column < width:
            if column == 0 or column == width-1:
                to_print += first_and_last
            else:
                to_print += middle_character
            column+=1

        print(to_print)
        
        row += 1



if len(sys.argv) < 2:
    print("Please pass height")
    sys.exit(1)

height = int(sys.argv[1])

print_box(height)


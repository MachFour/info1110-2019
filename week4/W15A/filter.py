import sys

# First have a check if the proper number of arguments are being passed to filter.py

if len(sys.argv) < 3:
    print("You need to pass in a filename and a character")
    sys.exit(1)

filename=sys.argv[1]
character=sys.argv[2]

# Open the file 
f = open(filename, 'r')

# Have a loop to read every line from the file
while True:
    line = f.readline() # Use readline to read only a SINGLE line
    if line == "": # If end of file (EOF), readline returns empty string
        break
    if line.startswith(character) == True:
        print(line) # Print without a new line since new lines exist at end of every line in file

f.close()

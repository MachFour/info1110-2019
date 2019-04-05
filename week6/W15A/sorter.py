import sys

if len(sys.argv) < 2:
    print("Filename not given")
    sys.exit(1)

# Open the file for reading
f = open(sys.argv[1], 'r')
# Read all the lines from the file and puts them in a list of strings
lines = f.readlines()
# Closes the file
f.close()

# This sorts the file
lines.sort()

# Using split to split before and after .
filename, ext = sys.argv[1].split('.')

# Make a new filename
newfilename = "{}-sorted.{}".format(filename, ext)

# Open the new file with 'w' mode
# 'w' - overwrites all the contents of the file
# 'a' - does not overwrite 

new_file = open(newfilename, 'w')

# Loop through the list of lines
i = 0
while i < len(lines):
    #print(lines[i], end='')
    # Write each line into the new file
    new_file.write(lines[i])
    i+=1

# Close the new file
new_file.close()


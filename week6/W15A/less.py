import sys

if len(sys.argv) < 2:
    print("Filename not given")
    sys.exit(1)

f = open(sys.argv[1], 'r')

line = f.readline()

while line != '':
    print(line, end='')
    user_input = input()
    if user_input == '': # Same as checking if user has pressed enter
        line = f.readline()
    elif user_input=='q':
        break

f.close()


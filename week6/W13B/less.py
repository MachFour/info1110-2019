import sys

if len(sys.argv) < 2:
    print("File name not provided.")
    sys.exit(257)

f = open(sys.argv[1], 'r')

while True:
    user_input = input()
    if user_input == '':
        line = f.readline()
        if line == '':
            break
        print(line, end='')
    elif user_input == 'q':
        break
    else:
        continue

f.close()

import sys
print("sys.argv is {}".format(sys.argv))
program_name = sys.argv[0]
print("The program name is", program_name)
if len(sys.argv) > 1:
    first_argument = sys.argv[1]
    print("The first argument is", first_argument)
else:
    print("There are no extra arguments")


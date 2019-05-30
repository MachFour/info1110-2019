def writer(filename, lines):
    # check types
    if not isinstance(filename, str) or not isinstance(lines, list):
        raise TypeError("Incorrect argument types")

    # check argument types inside the list
    i = 0
    while i < len(lines):
        if not isinstance(lines[i], str):
            raise ValueError("Cannot write non-string value to file")
        i += 1

    # now we open the file for writing
    f = open(filename, "w")

    i = 0
    while i < len(lines):
        f.write(lines[i] + "\n")
        i += 1
    f.close()

# Example:
example_lines = ['cats', 'dogs', 'ants', 'tigers', 'quokkas', 'wallabies',
        'kangaroos', 'orangutan', 'elephant']

try:
    writer("animals.txt", example_lines) # works
    writer("animals.txt", 1234) # TypeError
    writer(1, lines) # TypeError
except ValueError as e1:
    print(e1)
except TypeError as e2:
    print(e2)
finally:
    print("Finally... just for fun")


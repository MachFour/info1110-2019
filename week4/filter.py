import sys
# read the file name and the starting letter from sys.argv
if len(sys.argv) < 3:
    print("Please give a filename and a letter as arguments")
    sys.exit(111)
filename = sys.argv[1] # sys.argv is a list of strings
letter = sys.argv[2] # so each item is a string
text_file = open(filename, 'r') # 'r' means open for reading
while True:
    # read one line of text from the file
    line_text = text_file.readline()
    if line_text == "":
        # we have reached the end of the file
        break
    elif line_text[0] == letter[0]:
        print(line_text)
text_file.close() # have to close the file afterwards



# this string is joined with the previous one, even without using '+'
message = "This is Importer. I'm going to import the Importee, " \
    "because that is my job."

def main():
    # Here, 'message' is a global variable
    # we don't need the 'global' keyword because we aren't trying to modify it.
    print(message)
    print()

    import importee
    # After importing the Importee module, we gain access to its functions
    # and variables. Importing this way means that they are prefixed by the
    # module name (importee)
    print("Importer: The importee has another message:")
    print("'{:s}'".format(importee.message)) # print out a string in quotes

# This is a very common pattern/idiom in Python
# it means that all 'actual' code is inside a function.
# This way, everything can be tested!
if __name__ == "__main__":
    main()

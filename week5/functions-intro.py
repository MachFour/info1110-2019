#####################################
#             Functions             #
#####################################

# A function is a piece of code that captures the idea of 'doing an action'.
# For example 'print' is a function you already know, whose action is to
# output a string to the terminal.

# Using a function is called 'calling' a function, and the general syntax to
# call a function is: function_name(*), where * may be some arguments to the
# function (see below).

print("This code calls the 'print' function with 1 argument")

#####################################
#         Function arguments        #
#####################################

# Functions can take parameters or 'arguments', which can provide data needed
# to perform the action, or modify the behaviour of the action somehow.
# In Python, arguments can either be required or optional, with a default
# value.

# Arguments are placed inside the brackets and are separated by a comma.
# For example, print("Hello", name, "!") calls the print function with 3
# arguments.

# Another function example is the 'int' function, whose action is to convert a
# string to an integer. 'int' takes a string argument (required), which
# is the actual string to be converted to an integer. It also has an optional
# argument that specifies which number base to use. Normally, the default
# base is 10, i.e. our usual decimal system. But for converting numbers
# written in hexadecimal, like '0x4f', the base should be set to 16.

#####################################
# Returning values and side effects #
#####################################

# Functions can interact with the rest of your program's code in two ways.
# 1. They can return a variable/value to the place where the function is
#    called. This the same as how a mathematical function works: it produces
#    an output from some (or no) input. Here are some examples of functions
#    that work this way:

# A function taking one number argument (x) that returns its square, x^2
def square(x):
    return x*x

# Returns the first item in the list l, provided it contains at least one item.
# If l has no items, returns None.
def return_first(l):
    if len(l) > 0:
        return l[0]
    else:
        return None

# A function that returns a random number between 1 and 10. It takes no input.
import random
def random_number():
    return random_randint(1, 10)

# 2. Functions can also work by changing variables that exist outside
#    the function. This is called a 'side-effect' of the function.
#    You can think of the print function as working this way. Even though
#    you can't see it, there are variables in the Python software that
#    store text to be printed to the terminal. These kinds of functions
#    don't always return a value:

# print doesn't return a value
a = print("Just printing some random stuff")
if a == None:
    print("The 'print' function doesn't return anything")
    print("If you try to use the return value of a function that doesn't",
        "return anything, the return value will be None")

#    While not always true, sometimes functions can work by modifying
#    their input arguments. Look at the following example:

# This function modifies its argument list by changing the first item to 0,
# unless the list is empty. In which case, this function does nothing.
def change_first(l):
    if len(l) > 0:
        l[0] = 0
    else:
        # this means to do nothing.
        # I could have just not written an 'else' branch
        pass

a_list = [1, 2, 3]
print("Before changing: a_list is", a_list)
# call change_first with a_list as argument
change_first(a_list)
print("After changing: a_list is", a_list)


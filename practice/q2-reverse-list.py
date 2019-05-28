
#
# Question 2: Reversing a list
#

# Write a function reverse_list that takes a list or tuple argument
# and returns a new list, with the entries in reverse order.
# If the argument is not a list or tuple, the function should raise
# a TypeError with an appropriate message. (None is not a list or tuple)

# Do not use the inbuilt list.reverse or reversed() functions,
# for loops, the range() function, or list slice notation.

# Examples:
# reverse_list([1, 2, 3]) -> [3, 2, 1]
# reverse_list([]) -> []
# reverse_list(('a', 'b', 'c')) -> (('c', 'b', 'a'))


#
# Extension:
#

# Write another function reverse_list_inplace which takes a list argument
# (no tuples - why?), and modifies it to reverse its elements.
# You should not create a new list inside your function, and it should not
# return anything. Again if the input argument is not a list, the function
# should raise a TypeError with an appropriate message.

# The same restrictions apply as in the first part.

# Examples:
# l = [1, 4, 3, 2]
# reverse_list_inplace(l) # returns nothing
# print(l) # prints [2, 3, 4, 1]

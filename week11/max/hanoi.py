
# Recursive step of hanoi problem:
# move the bottom-most disc to destination
# then stack all remaining discs on the original pole

# Diagram, for recursive step A -> B:

# before:
# disc  A/1      B/2      C/3
#        |        |        |
#        |        |        |
#        o        |        |
#       ooo       |        |
#      ooooo      |        |
#     ooooooo     |        |

# after:
# disc  A/1      B/2      C/3
#        |        |        |
#        |        |        |
#        |        |        |
#        o        |        |
#       ooo       |        |
#      ooooo   ooooooo     |

# n is number of discs stacked (in increasing size) on pole A
def hanoi(n):
    pass

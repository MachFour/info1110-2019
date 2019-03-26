import sys
# return true if x is in the list l, else false
def check_in_list(l, x):
    i = 0
    while i < len(l):
        # check if the item at index i is equal to x
        if x == l[i]:
            return True
        i += 1
    # got to the end of the list, haven't found anything
    return False

def consonant_2(ch):
    # check ch against all the consonants
    all_consonants = [ 'b' ,'c' ,'d' ,'f' ,'g' ,'h' ,'j' ,'k' ,'l' ,'m' ,'n' ,'p' ,'q' ,'r' ,'s' ,'t' ,'v' ,'w' ,'x' ,'y' ,'z' ]
    #return ch in all_consonants
    is_consonant = check_in_list(all_consonants, ch)
    return is_consonant

def consonant(ch):
    # assume that ch is a string
    # assume that ch only contains alphabetical character
    if len(ch) != 1:
        # it can't be a single letter
        return False
    # at this point, we know the length of ch is 1
    c = ch[0]
    # c is a character/letter
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        return False
    else:
        return True

# program starts here
if len(sys.argv) < 2:
    print("Please give a character argument")
    sys.exit(1)
else:
    ch = sys.argv[1]
    is_consonant = consonant_2(ch)
    #is_consonant is a Boolean value
    # so I can use it like this:
    if is_consonant:
        print("'{}' is a consonant".format(ch))
    else:
        print("'{}' is not a consonant".format(ch))



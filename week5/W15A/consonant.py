def consonant(ch):
    if len(ch) != 1:
        return False

    if ch == 'a' or ch == 'e' or ch =='i' or ch =='o' or ch =='u':
        return False
    else:
        return True


def consonant_better(ch):
    if len(ch) != 1:
        return False
    
    if not ch.isalpha():
        return False

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    i = 0 # INITIALISE YOUR COUNTER
    while i < len(vowels): # HAVE A BREAK CONDITION
        if ch == vowels[i]: # LOGIC WITH LIST AND COUNTER
            return False
        i += 1 # INCREMENT YOUR COUNTER

    return True


print(consonant_better('b')) # True
print(consonant_better('a')) # False
print(consonant_better('wool')) # False
print(consonant_better('1')) # False

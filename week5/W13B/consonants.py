def consonant(ch):
    # TO DO
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        return False
    return True

def consonant_better(ch):
    if not ch.isalpha():
        return False

    if len(ch) != 1:
        return False

    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    while i < len(vowels):
        if ch == vowels[i]:
            return False
        i+=1

    return True

print(consonant_better('b'))
print(consonant_better('d'))
print(consonant_better('e'))
print(consonant_better('wool'))
print(consonant_better('1'))


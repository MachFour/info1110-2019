import time

def longest(words):
    if len(words) == 0:
        return None
    
    max_word = words[0] # Assume the first word in list of words to be the longest string

    i = 0
    while i < len(words):
        word = words[i]
        if len(word) >= len(max_word):
            max_word = word

        i += 1

#    i = len(words) - 1
#    while i >= 0:
#
#        word = words[i]
#        if len(word) > len(max_word):
#            max_word = word
#
#        i -= 1

    return max_word



dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']


#l = longest(dogs) # Retriever
#print(l)

dogs.append("Retrievar")
dogs.append("Retrievar")
dogs.append("Retrievar")
dogs.append("Retrievar")

l = longest(dogs) # Retrievar
print(l)

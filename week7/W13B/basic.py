# Write a function called longest(words) which will return the longest word from a list of words.
def longest(words):
    if len(words) == 0:
        return None
    
    max_word = words[0] # Assume max word to be the first element

    # Now iterate over all the words
    i = 0
    while i < len(words):
        if len(words[i]) >= len(max_word):
            max_word = words[i]
        i+=1

    return max_word





dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute', 'Retrievar']


l = longest(dogs)

print(l)


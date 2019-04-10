def longest(l):
    if l is None or len(l) == 0:
        return None

    max_len_string = l[0]
    
    i = 0
    while i < len(l):
        if len(max_len_string) <= len(l[i]):
            max_len_string = l[i]
        i+=1

    return max_len_string

def longest2(l):
    return if len(l) != 0 max(l,key=lambda x : len(x) ) else None

def shortest(l): 
    if l is None or len(l) == 0:
        return

    min_len_string = l[0]
    
    i = 0
    while i < len(l):
        if len(min_len_string) >= len(l[i]):
            min_len_string = l[i]
        i+=1

    return min_len_string

def av_len(l):
    if l is None or len(l) == 0:
        return None

    sum_len = 0
    i = 0
    while i < len(l):
        sum_len += len(l[i])
        i+=1

    return sum_len/len(l)

def start_count(l, char):
    if l is None or len(l) == 0:
        return None

    i = 0
    count = 0
    while i < len(l):
        
        word = l[i]
        first_character = word[0]

        if first_character == char:
            count+=1
        i+=1

    return count



dogs = ['Collie', 'Retriever', 'Corgi', 'Labrador', 'Husky', 'Malamute']

l = longest2(dogs) # Retriever
s = shortest(dogs) # Husky
a = av_len(dogs) # 6.8333333...
c = start_count(dogs, 'C') # 2
d = start_count(dogs, 'D') # 0
h = start_count(dogs, 'H') # 1

print(l, s, a, c, d, h)

# separate function to find total length of words
def total_length(words):
    sum_length = 0
    i = 0
    while i < len(words):
        word = words[i]
        if not isinstance(word, str):
            raise ValueError("Error: {} at index {} is not a string".format(word, i))
        sum_length += len(words[i])
        i += 1
    return sum_length

def av_len(words):
    if len(words) == 0:
        return 0
    # we guaranteed that that len(words) != 0,
    # so we are definitely not dividing by 0 here.
    average_length = total_length(words)/len(words)
    return average_length

def test1():
    import sys
    words = sys.argv[1:]
    print("Words: ", words)
    avg = av_len(words)
    print("Average length:", avg)

def test2():
    # what happens when we don't use words?
    words = ("these", "are", "some", 0, "words")
    avg = av_len(words)
    print("Average length:", avg)

# use this to test various inputs
if __name__ == "__main__":
    try:
        test2()
    except ValueError as e:
        print(e)

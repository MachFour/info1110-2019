# Most basic programming techniques, but more code needed
def longest1(words):
    if len(words) == 0:
        return None

    # the list is not empty, otherwise the function would have returned
    longest_len = len(words[0])
    longest_index = 0
    index = 0
    while index < len(words):
        next_word = words[index]
        if len(next_word) >= longest_len: # why don't we use '>' instead?
            # save the new maximum length and which word it was
            longest_len = len(next_word)
            longest_index = index

        index += 1
    return words[longest_index]

# using more python tricks:
# less code... but is it faster?

def longest2(words):
    if not words:
        return None
    # This iterates through the list once, just to find the maximum
    longest_length = max(len(w) for w in words)
    # we only need to save just the word this time.
    longest_word = words[0]
    for w in words:
        if len(w) == longest_length:
            longest_word = w
            # what happens if we break here?

    return longest_word

def test_all():
    # test it out
    w1 = ['one', 'of', 'these', 'words', 'is', 'the', 'longest']
    w2 = ['two', 'of', 'these', 'words', 'are', 'seemingly', 'elongated']
    w3 = []

    expected_longest = ['longest', 'elongated', None]
    print("First method:", end="\n\n")
    longest1_test = [longest1(w1), longest1(w2), longest1(w3)]

    print("List 1 longest word is", longest1_test[0])
    print("List 2 longest word is", longest1_test[1])
    print("List 3 longest word is", longest1_test[2])
    print()
    if longest1_test != expected_longest:
        print("This wasn't what was expected, oh no!")
        print("Expected: ", expected_longest)
    else:
        print("This is what was expected, yay")

    print(end="\n\n")

    print("Second method:", end="\n\n")
    longest2_test = [longest2(w1), longest2(w2), longest2(w3)]

    print("List 1 longest word is", longest2_test[0])
    print("List 2 longest word is", longest2_test[1])
    print("List 3 longest word is", longest2_test[2])
    print()
    if longest2_test != expected_longest:
        print("This wasn't what was expected, oh no!")
        print("Expected: ", expected_longest)
    else:
        print("This is what was expected, yay")

# this prevents the tests from running if you import this file as a module
if __name__ == "__main__":
    test_all()


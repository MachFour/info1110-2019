import strings

test_cases = [
    'AAaaAA',
    'xyz',
    'BBB',
    None,
    'AAAaa',
    'AaAaA'
]

expected_outputs = [
    2,
    0,
    -1,
    -1,
    3,
    -1
]

i = 0 
while i < len(test_cases):
    print("Test #{}".format(i+1))
    input_string = test_cases[i]
    expected_output = expected_outputs[i]
    try:
        actual_output = strings.get_first_lowercase_pair(input_string)
    except Exception as e:
        print("{} occurred for input: {}".format(e, input_string))

    if expected_output != actual_output:
        print("Test case failed!")
        print("Input: {}".format(input_string))
        print("Expected Value: {}".format(expected_output))
        print("Actual Value  : {}".format(actual_output))

    i+=1

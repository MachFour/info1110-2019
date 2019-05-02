import strings


test_cases = [
        "AAaaAA",
        "xyz",
        "AAA",
        None,
        "AaaA",
        "AAa",
        1,
        "1234"
        ]

expected_outputs = [
        2,
        0,
        -1,
        -1,
        1,
        2,
        -1,
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
        print("{} caused by input: {}".format(e, input_string)) 
        i+=1
        continue

    if actual_output != expected_output:
        print("Something went wrong")
        print("Input: {}".format(input_string))
        print("Expected: {}".format(expected_output))
        print("Actual:   {}".format(actual_output))

    i+=1 







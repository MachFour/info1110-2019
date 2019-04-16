import strings
input_strings = [
        'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA',
        'a s a s a s a',
        'BBBBBBBBBaa',
        'AaAaAaAaAaAaAaA'
        ]
output_numbers = [
        0,
        -1,
        -1,
        9,
        -1
        ]

i = 0
while i < len(input_strings):
    print("Test case {}".format(i))
    expected_output = output_numbers[i]
    actual_output = strings.get_first_lowercase_pair(input_strings[i])
    if actual_output != expected_output:
        print("Test case failed!")
        print("Input:", input_strings[i])
        print("Expected output:", expected_output)
        print("Actual output:", actual_output)
    print()
    i += 1




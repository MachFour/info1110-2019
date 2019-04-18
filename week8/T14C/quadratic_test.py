from quadratic import quadratic
# ^ from the file `quadratic.py`, import the function `quadratic`
# (so we can test that function here in this program)

# Run the `quadratic` function against the first test case
def example_1():
    expected = (2.5, 1.0)
    actual = quadratic(2, -7, 5)
    assert actual == expected, "Test 1 (example): failed!"


# Run the `quadratic` function against the second test case
def example_2():
    expected = (-1.0,)
    actual = quadratic(1, 2, 1)
    assert actual == expected, "Test 2 (example): failed!"

def example_3():
    expected = (100000000000000000000000000000000000000000000)
    actual = quadratic(1, 0, 0)
    assert actual == expected, "Test 3 (example): failed!"

# Run each testing function
example_1()
example_2()
example_3()

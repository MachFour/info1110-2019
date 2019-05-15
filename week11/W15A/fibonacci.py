def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")

    print("fibonacci({:d})".format(n))
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # recursive formula:
        # F(n) = F(n-1) + F(n-2)
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # else
    # i.e. F(n-2) and F(n-1)
    two_steps_back = 0
    one_step_back = 1

    # we just need to repeat the Fibonacci step the
    # correct number of times
    i = n - 1 # n = 2 -> i starts at 1
    while i > 0: # n = 2 -> loop iterates once
        # fibonacci step: F(n) = F(n-1) + F(n-2)
        next_number = one_step_back + two_steps_back
        # update the previous steps
        two_steps_back = one_step_back
        one_step_back = next_number
        i -= 1
    return next_number




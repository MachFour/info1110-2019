def fibonacci(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    print("fibonacci({:d})".format(n))
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        # Recursive definition of the Fibonacci series
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci2(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # n >= 2
    #f(2) = f(1) + f(0)
    #f(3) = f(2) + f(1)
    #f(4) = f(3) + f(2)
    #f(n) = f(n-1) + f(n-2)
    one_step_back = 1 # initially f(1)
    two_steps_back = 0 # initially f(0)
    i = 2
    while i <= n:
        # initially f(2), always == f(i)
        next_number = one_step_back + two_steps_back
        # update the previous results
        two_steps_back = one_step_back
        one_step_back = next_number
        i += 1
    # shoudld have next_number == fibonacci(n)
    return next_number



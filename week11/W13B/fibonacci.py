def fibonacci(n):
    if n < 0:
        raise ValueError("n can't be negative!")
    # just for curiosity
    print("fibonacci({:d})".format(n))
    # base case(s)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # else
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_iterative(n):
    if n < 0:
        raise ValueError("n can't be negative!")
    # just for curiosity
    print("fibonacci({:d})".format(n))
    # base case(s)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # else
    # F(n) = F(n-1) + F(n-2)
    # previous two fibonacci sequence values
    two_steps_behind = 0
    one_step_behind = 1
    i = n
    while i > 1: # iterate until 'base case'
        next_number = two_steps_behind + one_step_behind
        # update previous values
        two_steps_behind = one_step_behind
        one_step_behind = next_number
        i -= 1
    return next_number

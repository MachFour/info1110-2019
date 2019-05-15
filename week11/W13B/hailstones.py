def hailstone_calculation(n):
    if n % 2 == 1:
        # n odd
        return n*3 + 1
    else:
        # n even
        return n // 2

def hailstones(n):
    if n <= 0:
        raise ValueError("n must be positive")
    elif n == 1:
        # base case
        return [1]
    else:
        next_value = hailstone_calculation(n)
        # returns a list of 'hailstone steps' ending in 1
        remaining_steps = hailstones(next_value)
        return [n] + remaining_steps


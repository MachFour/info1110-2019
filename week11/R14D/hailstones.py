def hailstone_step(n):
    if n % 2 == 1:
        return 3*n + 1
    else:
        return n // 2

def hailstones(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a positive integer")
    if n == 1:
        # base case
        return [1]
    else:
        # recursive case
        next_number = hailstone_step(n)
        return [n] + hailstones(next_number)


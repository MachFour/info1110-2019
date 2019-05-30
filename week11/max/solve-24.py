
target = 24

class Solution:
    def __init__(self, target, first_number):
        self.target = target
        self.first_number = first_number
        self.operations = [''] # initial value just for printing

    def __repr__(self):
        return "{:d}{:s} = {:d}".format(self.first_number,
                " ".join(self.operations), self.target)

    def add_operation(self, op):
        self.operations.append(op)

    def add_operation_pre(self, op):
        self.operations.insert(0, op)

def solve(target, numbers):
    if len(numbers) == 0:
        # base case (should not be reached during normal recursion)
        return None
    elif len(numbers) == 1:
        # base case
        if numbers[0] == target:
            return Solution(target, numbers[0])
        else:
            return None
    # Now try each of the operations in turn on each number
    # (note: don't need else due to return statements above)

    solution = None

    i = 0
    while i < len(numbers):
        # try an operation using this number, and recurse on the rest
        n = numbers[i]
        rest = numbers[:i] + numbers[i+1:] # exclude number at index i
        # add:
        solution = solve(target - n, rest)
        if solution:
            solution.add_operation("+ {:d}".format(n))
            break
        # add 2:
        solution = solve(n - target, rest)
        if solution:
            solution.add_operation_pre("{:d} +".format(n))
            break
        # subtract
        solution = solve(target + n, rest)
        if solution:
            solution.add_operation("- {:d}".format(n))
            break
        # multiply 1
        solution = solve(target / n, rest)
        if solution:
            solution.add_operation("* {:d}".format(n))
            break
        # multiply 2
        if target != 0:
            solution = solve(n / target, rest)
            if solution:
                solution.add_operation_pre("{:d} *".format(n))
                break
        # divide
        solution = solve(target * n, rest)
        if solution:
            solution.add_operation("/ {:d}".format(n))
            break
        i += 1

    if solution:
        solution.target = target
        return solution
    else:
        # it's nice to explicitly show that we want to return None
        return None

if __name__ == "__main__":
    pass

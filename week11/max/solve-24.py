
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
    # Now try each of the operations in turn
    # (note: don't need else due to return statements above)

    # add:
    solution = solve(target - numbers[0], numbers[1:])
    if solution:
        solution.add_operation("+ {:d}".format(numbers[0]))
        solution.target = target
        return solution
    # subtract
    solution = solve(target + numbers[0], numbers[1:])
    if solution:
        solution.add_operation("- {:d}".format(numbers[0]))
        solution.target = target
        return solution
    # multiply
    solution = solve(target / numbers[0], numbers[1:])
    if solution:
        solution.add_operation("* {:d}".format(numbers[0]))
        solution.target = target
        return solution
    # divide
    solution = solve(target * numbers[0], numbers[1:])
    if solution:
        solution.add_operation("/ {:d}".format(numbers[0]))
        solution.target = target
        return solution



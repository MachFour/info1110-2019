import sys
import math

i = complex(imag=1) # i^2 = -1

def quadratic(a, b, c):
    disc_squared = b**2 - 4*a*c # the quadratic discriminant
    if disc_squared == 0:
        # single solution
        solution = (-b / (2*a), )
    else:
        if disc_squared > 0:
            # two real solutions
            disc = math.sqrt(disc_squared) # this is positive
        else:
            # two complex_solutions:
            disc = i*math.sqrt(-disc_squared)
        # same formula for both
        solution = (-b+disc / (2*a), -b-disc / (2*a))
    # what's the type of solution?
    return solution

# catch IndexError and int (-> float) conversion errors
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
x_1, x_2 = quadratic(a, b, c) # unpack the returned tuple

print('The equation {}x^2 + {}x + {} = 0 has these solutions:'.format(a, b, c))
print('x={:.2f} and x={:.2f}'.format(x_1, x_2))

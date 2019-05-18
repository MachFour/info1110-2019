
# Recursive step of hanoi problem:
# stack all non-largest discs on the third pole
# then move the largest disc to desired destination

# Diagram, for recursive step A -> B:

# before:
# disc  A/1      B/2      C/3
#        |        |        |
#        |        |        |
#        o        |        |
#       ooo       |        |
#      ooooo      |        |
#     ooooooo     |        |

# after:
# disc  A/1      B/2      C/3
#        |        |        |
#        |        |        |
#        |        |        |
#        |        |        o
#        |        |       ooo
#        |     ooooooo   ooooo

class Hanoi:
    def __init__(self, n):
        # number of discs
        self.n = n
        # which poles to use
        self.origin = 0
        self.destination = 1
        self.intermediate = 2

        self.game_state = Hanoi.initial_hanoi_game(n)

    def do_game(self):
        self.print_hanoi()
        self.move_n(self.n, self.origin, self.destination,
                self.intermediate)

    def print_hanoi(self):
        """Prints a picture of the hanoi game.
        a, b and c are lists containing the sizes of the discs from
        bottom to top. Units are radius, the smallest possible disc
        having a radius of 1. 0 or negative will leave a space."""
        a, b, c = self.game_state
        max_radius = max(a + b + c)
        max_diameter = 2*max_radius - 1
        max_height = self.n + 1
        # two spaces between towers (one on each side)
        total_width = 3*(max_diameter + 2)
        for row in range(max_height):
            print(" ", end="")
            Hanoi.print_tower_slice(a, row, max_height, max_diameter)
            print("  ", end="")
            Hanoi.print_tower_slice(b, row, max_height, max_diameter)
            print("  ", end="")
            Hanoi.print_tower_slice(c, row, max_height, max_diameter)
            print(" ")
        print("".join(["="]*total_width))
        print()


    @staticmethod
    def print_tower_slice(tower, row, max_height, tower_width):
        """Prints one disc in one tower based on the current row and
        maximum height of the printout"""
        virtual_index = max_height - 1 - row
        if virtual_index >= len(tower):
            radius = 0
        else:
            radius = max(0, tower[virtual_index])
        # basically print out 2*radius - 1 number of disc
        # in between the remaining number of spaces
        if radius:
            disc_chars = 2*radius - 1
        else:
            disc_chars = 0
        spaces_each_side = (tower_width - disc_chars)//2
        print("".join([" "]*spaces_each_side), end="")
        for _ in range(disc_chars):
            print('o', end="")
        if not disc_chars:
            # print the tower stem
            print("|", end="")
        print("".join([" "]*spaces_each_side), end="")


    # returns a hanoi game state corresponding to
    # having n discs of increasing diameter
    # (top to bottom) stacked on the leftmost pole
    @staticmethod
    def initial_hanoi_game(n):
        return [list(range(n, 0, -1)), [], []]

    def move_top(self, origin, destination):
        top = self.game_state[origin].pop()
        self.game_state[destination].append(top)
        self.print_hanoi()

    def move_n(self, n, origin, destination, other):
        if n <= 0:
            # base case: move nothing
            return
        elif n == 1:
            self.move_top(origin, destination)
        else:
            # n - 1 smaller discs
            self.move_n(n-1, origin, other, destination)
            # largest disc
            self.move_top(origin, destination)
            # n - 1 smaller discs
            self.move_n(n-1, other, destination, origin)

# to use from the command line:
# python hanoi.py <height>

if __name__ == "__main__":
    import sys
    height = 0
    try:
        height = int(sys.argv[1])
        if height <= 0:
            print("Height must be a positive integer.")
            sys.exit(1)
    except ValueError:
        print("Height must be a positive integer.")
        sys.exit(1)
    except IndexError:
        print("Usage: python {} <height>".format(sys.argv[0]))
        sys.exit(1)

    game = Hanoi(height)
    game.do_game()

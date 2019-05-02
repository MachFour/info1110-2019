import math
class Circle:
    # class variable
    # Accessing the class variable: Circle.PI
    PI = math.pi
    # c = Circle()
    # c.get_wiki_page()
    @staticmethod
    def get_wiki_page():
        return "https://en.wikipadia.org/foaijfa"

    def __init__(self, radius):
        self.radius = radius

    # used in print()
    def __str__(self):
        return "Circle with radius {:.2f}".format(self.radius)

    # Used in printing lists
    def __repr__(self):
        return "Circle({:.2f})".format(self.radius)

    def get_area(self):
        # formula: pi*radius^2
        return Circle.PI*(self.radius ** 2)

c1 = Circle(2)
c2 = Circle(5)
c3 = Circle(4)




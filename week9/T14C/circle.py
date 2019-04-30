import math

class Circle:
    # attributes: radius
    # methods: get_area()
    # class methods: get_wiki_page()

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "Circle with radius: " + str(self.radius)

    def __repr__(self):
        return str(self)

    # instance methods always require 'self'
    def get_area(self):
        return math.pi*(self.radius**2)

    # Class method: doesn't need self
    def get_wiki_page():
        return 'https://en.wikipedia.org/wiki/Circle'

c1 = Circle(2)
c2 = Circle(5)
c3 = Circle(4)



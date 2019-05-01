import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def calculate_sum_area(circles):
        area_sum = 0.0
        i = 0
        while i < len(circles):
            area_sum += circles[i].get_area()
            i+=1
        
        return area_sum

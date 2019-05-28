class Person:
    # class variables
    counter = 0
    current_year = 2019
    is_christmas = False

    # raise a ValueError if the full_name is not a string
    # or doesn't look like a full name
    def check_full_name(full_name):
        pass

    # raise a ValueError if year is not a positive integer
    def check_year(year):
        pass

    def __init__(self, full_name, year):
        # instance variables
        # increment number of people created
        Person.counter += 1
        # record number of people currently created
        # as instance variable
        self.id = Person.counter

        # check that full_name is a first and last name
        # 1. make sure it's a string
        # 2. check that it's two words separated by a space
        Person.check_full_name(full_name)
        # no problems - go ahead and assign
        self.full_name = full_name

        # make sure that year is a positive integer
        Person.check_year(year)
        self.year = year

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, new_full_name):
        # check it's a valid name
        Person.check_full_name(new_full_name)
        # now overwrite the instance variable
        self.full_name = new_full_name

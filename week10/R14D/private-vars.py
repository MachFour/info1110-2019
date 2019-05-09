class PrivateVariable:
    def __init__(self, value):
        # this instance variable won't be visible from outside the class
        self.__value = value

    def __repr__(self):
        return "Private variable with value {}".format(self.__value)

    def get_value(self):
        return self.__value

    #def set_value(self, new_value):
    #    if new_value % 2 == 0:
    #        raise ValueError("I won't accept value {}, " \
    #                "sorry!".format(new_value))
    #    else:
    #        self.__value = new_value

if __name__ == "__main__":
    p = PrivateVariable(50)
    print("Object's __repr__ function:", p)
    print()
    print("Accessing value from getter method:")
    print("the value of p is", p.get_value())
    print()
    print("Accessing value from outside class:")
    print("the value of p is", p.__value)




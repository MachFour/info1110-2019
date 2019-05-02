class Parent:
    def __init__(self, name):
        print("Parent constructor")
        self.name = name

    def parent_method(self):
        print("Parent method")


class Child(Parent):
    def __init__(self, name): 
        print("Child constructor")
        super().__init__(name)

    def child_method(self):
        print("Child method")

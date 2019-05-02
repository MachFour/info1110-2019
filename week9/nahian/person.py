class Person:
    """
    The person class simulates the attributes and actions of a person.
    """

    species = "Homo Sapiens" 
    """
    This is a class variable. Notice that the self key word is missing. 
    This attribute is shared by all persons and is non-unique.
    """

    def __init__(self, name, age):
        """
        This is the constructor function for the class Person.
        All objects which belong to Person, e.g. Bob, Alice will have their own
        unique names and ages.
        """
        self.name = name
        self.age = age

    
    def introduce(self):
        """
        This is an instance method. This means, only a unique object can
        call this function. e.g. Alice.introduce() or Bob.introduce()
        """
        print("Hi, I am {}. I am {} years old.".format(self.name, self.age))

    def say_birthyear(self, current_year):
        """
        Similar to the previous method, this method is also invoked
        using a specific object, e.g. Alice.say_birthyear(2019),
        but this method takes in an additional parameter
        @param : current_year -> int
        """
        print("I was born in {}.".format(current_year-self.age))

    def converse(p1, p2):
        """
        This is a class/static method. Notice that the self keyword is missing here again.
        This means that a unique object will not invoke this method, rather the class
        will.
        Usage: Person.converse(Alice, Bob)
        """

        conversation = """{0}: Hi! I am {0}. Nice to meet you.\n{1}: Hello! My name is {1}. Nice to meet you too!""".format(p1.name, 
                p2.name)

        print(conversation)



# if __name__ == "__main__":
    
    #Alice = Person("Alice", 22)
    #Bob = Person("Bob", 21)

    #Person.converse(Alice, Bob)

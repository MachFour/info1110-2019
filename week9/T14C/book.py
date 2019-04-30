
# we're defining a class called Book
class Book:
    # this function is called when a Book object is first created
    def __init__(self, title, author, year, url):
        self.title = title
        self.author = author
        self.year = year
        self.url = url

    # returns the age of the book in years
    def how_old(self):
        return 2019 - self.year

    def length_of_title(self):
        return len(self.title)

    # this is a class method
    def default_url():
        return 'www.google.com'

    # this function is called when a string representation of a Book
    # object is needed, for example in print()
    # Note: this function must RETURN a string, not PRINT.
    # (What do you think would happen if you printed it instead?)

    def __str__(self):
        return "'{}', a book by {} ({:d}) [{}]".format(
                self.title, self.author, self.year, self.url)

    # Now comment out this function, and try to print() a book out.
    # What do you see?

my_book = Book("The Very Hungry Caterpillar", "Eric Carle", 1969, "www.tvhc.com")

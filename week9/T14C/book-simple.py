# we're defining a class called Book
class Book:
    # this function is called when a Book object is first created
    def __init__(self, title, author, year, url):
        self.title = title
        self.author = author
        self.year = year
        self.url = url

book = Book("The Very Hungry Caterpillar", "Eric Carle", 1969, "www.tvhc.com")

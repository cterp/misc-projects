# The Shelf class initializes a library with five categories (mystery, classic, poetry, biography, and textbook) and 7
# books. Each shelf knows what books it contains. This class includes methods to count how many books are in the
# library, print the contents of both an individual shelf and the entire library, and count the number of shelves.
class Shelf(object):

    # Initializes the library with 7 books across 4 shelves, with one empty shelf (total of 5 shelves).
    shelves = {
        'Mystery': {'Murder on the Orient Express':'Agatha Christie', 'Faceless Killers':'Henning Mankell'},
        'Classic': {'Wuthering Heights':'Emily Bronte', 'Hamlet':'William Shakespeare'},
        'Poetry': {},
        'Biography': {'The Last Viking: The Life of Roald Amundsen':'Stephen R. Brown', 'Marie Curie: A Life':'Susan Quinn'},
        'Textbook': {'Classical Mechanics':'John Taylor'}
    }

    # Prints the content of the whole library, shelf by shelf.
    def content_of_all_shelves(self):
        print "Listed below are the contents of this whole library:\n"
        for category in self.shelves:
            self.print_contents_one_shelf(category)

    # Returns a count of how many books are in the library.
    def number_of_books(self):
        num_of_books = 0
        for category in self.shelves:
            for book in self.shelves[category]:
                num_of_books += 1
        return num_of_books

    # Returns the number of shelves in the library.
    def number_of_shelves(self):
        return len(self.shelves.keys())

    # Prints the contents of a specific shelf, given its name. Will print an error if the shelf doesn't exist.
    def print_contents_one_shelf(self, shelf_name):

        if not shelf_name in self.shelves.keys():
            print "Sorry, this library doesn't have a " + shelf_name.lower() + " shelf.",
        elif len(self.shelves[shelf_name].keys()) == 0:
            print "The " + shelf_name.lower() + " shelf is empty.",
        else:
            print "The " + shelf_name.lower() + " shelf contains the following books:"
            for key in self.shelves[shelf_name]:
                print key + " by " + self.shelves[shelf_name][key],
        print "\n"

# The Library class contains methods that print a greeting to the user and report how many books and shelves are
# in the library.
class Library(Shelf):
    def print_greeting(self):
        print "Welcome to your local public library!"

    def number_of_shelves(self):
        num_shelves = super(Library, self).number_of_shelves()
        num_books = super(Library, self).number_of_books()
        print "There are %d shelves in this library with a total of %d books." % (num_shelves, num_books)



# The Book class represents objects that have title, author, and category attributes. It is possible to add and remove
# books from a given shelf by calling the enshelf() and unshelf() methods, respectively.
class Book(Shelf):
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    # Adds a book to the shelf
    def enshelf(self):
        print "Adding %s by %s to your library." % (self.title, self.author)
        if not self.category in self.shelves:
            self.shelves[self.category] = {self.title:self.author}
        elif self.title in self.shelves[self.category]:
            print "This book is already on the shelf; a second copy was not added."
        else:
            self.shelves[self.category][self.title] = self.author

    # Removes a book from the shelf
    def unshelf(self):
        print "Removing %s by %s from your library." % (self.title, self.author)
        if not self.title in self.shelves[self.category]:
            print "This book isn't in your library. Did you lose it?"
        else:
            del self.shelves[self.category][self.title]


# commands that show this works

my_library = Library() # create a new Library object

my_library.print_greeting() # print a greeting
print " ------------------ "
my_library.number_of_shelves() # print how many shelves and books there are in the library
print " ------------------ "
my_library.content_of_all_shelves() # Print out the contents of the whole library shelf-by-shelf
print " ------------------ "
my_library.print_contents_one_shelf('Poetry') # Print the contents of just the poetry shelf
print " ------------------ "
my_library.print_contents_one_shelf('Sci-fi') # Print the contents of a shelf that doesn't exist
print " ------------------ "

# create a Book object and try to enshelf a book that's already in the library
my_book = Book(title="Marie Curie: A Life", author="Susan Quinn", category="Biography")
my_book.enshelf()
print " ------------------ "

# add a book in a category that doesn't exist in the library
my_book = Book(author="Allen Downey", title="Think Python", category="Technology")
my_book.enshelf()
my_library.print_contents_one_shelf('Technology')
print " ------------------ "

# remove the technology book that was just added
my_book.unshelf()
my_library.content_of_all_shelves() # the technology category is still there, but is now empty
print " ------------------ "

# try to remove a book that isn't in the library
my_book.unshelf() # my_book is still "Think Python"


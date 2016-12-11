import json 
def open_library(filename):
    # Create empty dictionaries just in case the library file is empty
    students = {}
    books = {}

    # Open the library file encoded in JSON and load it into the data object
    # We use the with keyword so we don't have to explicitly close the file
    # later.
    #
    # Alternatively you could use:    #
    #  f = open(filename)
    #  data = json.load(f)
    #  f.close()
    #
    # and accomplish the same thing.

    with open(filename) as f:
        data = json.load(f)

    # If there are students or books in the library,    # overwrite the empty dictionaries we created
    if data['students'] != {}:
        students = data['students']

    if data['books'] != {}:
        books = data['books']
    # Return the data we loaded from the file
    return students, books

def add_book(filename, isbn, title, author):
    # Here's a start
    students, books = open_library(filename)

    # Now how can we add books to the data?
    # In the space below, write code that adds the key isbn
    # and the value {'title':title, 'author':author}
    # to the books object.

    books[isbn] = {'title': title, 'author':author}
    
    # Finally, write code that writes the new data to the library
    # Do we need to return anything?
    with open(filename) as f:
        json.dump({'students':students,'books':books}, f)
        
    
def remove_book(filename, isbn):
    students, books = open_library(filename)

    # How can we *remove* an item from a dictionary?
    # Write code to delete the book keyed by isbn in the space below

    if 'isbn' in books:
        del books['isbn']
    # Now write code that saves the new version of the data to your library
    with open(filename) as f:
        json.dump ({'students' : students, 'books' : books} ,f)
        
def check_out(filename, isbn, s_id):
    students, books = open_library(filename)

    # Find a way to mark a book as checked out. Be sure to associate
    # the book with the student who borrowed it!
    
    checked_out = {}
    if 'isbn' in books:
        checked_out.updated(books[isbn])

    # And again save the data here
    with open(filename) as f:
        json.dump({'students' : students, 'books' : books} ,f)
        
    pass


def return_book(filename, isbn):
    students, books = open_library(filename)

    if 'isbn' in checked_out:
        books.updated(checked_out)
        
    # Now ensure that the book is no longer checked out and save the changes
    # to the library.
    
    with open(filename) as f:
        json.dump({'students' : students, 'books' : books} ,f)
    
    pass


def status(filename):
    students, books = open_library(filename)
    
    if books[isbn] == True:
        return book[isbn]
    else:
        return checked_out[isbn]
    
    # Print out two lists - one of all books currently checked out,
    # and one of all available books.
    
    with open(filename) as f:
        json.dump({'students' : students, 'books' : books} ,f)
    pass


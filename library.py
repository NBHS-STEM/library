import json


def open_library(filename):
    students = {}

    books = {}

    with open(filename) as f:
        data = json.load(f)

    if data['students'] != {}:
        students = data['students']

    if data['books'] != {}:
        books = data['books']

    return students, books


def add_book(filename, isbn, title, author):
    students, books = open_library(filename)

    isbn = input("what is the isbn?")
    title = input("what is the title?")
    author = input("who is the author?")

    books[isbn] = {'title': title, 'author': author}

    print("Book has been sucesfully added to the library!!")

    with open(filename, 'w') as f:
        json.dump({'students': students, 'books': books}, f)


def remove_book(filename, isbn):
    students, books = open_library(filename)

    for key in books:
        print(key, books[key])
        print('')
        print('')

    isbn = input("what is the isbn of the book you wish to delete?")

    if isbn in books:
        del books[isbn]

    print("book has been deleted")

    with open(filename, 'w') as f:
        json.dump({'students': students, 'books': books}, f)


def check_out(filename, isbn, s_id):
    students, books = open_library(filename)

    # Find a way to mark a book as checked out. Be sure to associate
    # the book with the student who borrowed it!
    print("ALL BOOKS IN LIBRARY")
    for key in books:
        print(key, books[key])
        print('')
        print('')

    s_id = input("what is ur ID?")

    isbn = input('what book do you want to check out(choose by isbn)?')

    if isbn not in books:
        print("Book is not in Library")
    else:
        books[isbn]['checked_out'] = s_id
        print('%s has been checked out' % isbn)

    # And again save the data here

    with open(filename, 'w') as f:
        json.dump({'students': students, 'books': books}, f)


def return_book(filename, isbn):
    students, books = open_library(filename)
    isbn = input("what book do you want to return(by isbn)?")

    if books[isbn]['checked_out']:
        del books[isbn]['checked_out']
        print("%s has been returned" % isbn)

    else:
        print("book is not in Library or book is already checked in")

    # Now ensure that the book is no longer checked out and save the changes
    # to the library.
    with open(filename, 'w') as f:
        json.dump({'students': students, 'books': books}, f)


def status(filename, isbn, ):
    students, books = open_library(filename)
    # Print out two lists - one of all books currently checked out,
    # and one of all available books.


    print("Do you want:")
    print("1. ALL BOOKS")
    print("2. BOOKS CHECKED OUT")
    print("choose 1 or 2")
    option = input("")
    if option == '1':

        print("              ALL BOOKS IN LIBRARY:")
        for key in books:
            print(key, books[key])
            print('')
            print('')

    elif option == '2':
        print("          BOOKS THAT HAVE BEEN CHECKED OUT:")

        if books[isbn]["check_out"]:
            for key in books:
                print(key, books[isbn]["check_out"])
        http://stackoverflow.com/questions/3817529/syntax-for-creating-a-dictionary-into-another-dictionary-in-python
    else:
        print('Invalid selection.')


# Main loofor key, value in mydic.iteritems() :



while True:
    print('=' * 21)
    print('   Library System')
    print('=' * 21)
    print('1. Add books to the library')
    print('2. Remove books from library ')
    print('3. Check out book from library ')
    print('4. Return book')
    print('5. Library status')
    print('Q. Quit')
    m = input('Select an option from above or enter Q to quit. ')
    if m.upper() == 'Q':
        break

    # replace 'pass' with appropriate inputs and function calls.
    elif m == '1':
        add_book('data/test.json', 'isbn', 'title', 'author')
    elif m == '2':
        remove_book('data/test.json', 'isbn')
    elif m == '3':
        check_out('data/test.json', 'isbn', 's_id')
    elif m == '4':
        return_book('data/test.json', 'isbn')
    elif m == '5':
        status('data/test.json', 'isbn', )
    else:
        print('Invalid selection.')

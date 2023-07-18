"""
STUDENT LIBRARY
Implement a student library system using OOPs while students can 
borrow a book from the list of books.
Create a seperate library and student class.
Your program must be menu driven
You are free to choose methods and attributes of your choice
to imlement this fucntionality
"""

class Library:
    
    def __init__(self,ListOfBooks):
        self.books = ListOfBooks

    def displayAvaliableBooks(self):
        print("The books present in the librabry are: ")
        for book in self.books:
            print("\t" + book)

    def borrowbook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe")
            self.books.remove(bookName)
            return True
        else:
            print("This book is unavilable")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning")

class Student:

    def requestBook(self):
        self.book= input("Enter the name of the book you want to borrow : ")
        return self.book
        
    def retrunBook(self):
        self.book= input("Enter the name of the book you want to return : ")
        return self.book

if __name__== "__main__":
    centrallibrary = Library(["Science","Maths","social","Computer","English"])
    student = Student()
    #centrallibrary.displayAvaliableBooks()
    while(True):
        welcomeMsg = '''Welcome to Central Library. 
        Please choose and option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice : "))
        if a==1:
            centrallibrary.displayAvaliableBooks()
        elif a==2:
            centrallibrary.borrowbook(student.requestBook())
        elif a==3:
            centrallibrary.returnBook(student.retrunBook())
        elif a==4:
            print("Thanks for choosing central library")
            exit()

        else:
            print("Invalid Choice!")
# s={1,2,3,3,2,1,4}
# result=0
#
# for num in s:
#     result^=num
# print(result)
# a={1,2,3,4}
# b={1,5,4,3}
# print(a.intersection(b))
from phonebook import display

#OOPS

# class Employee:
#     def display(self):
#         print('hello')
#
# #objec
# e1=Employee()#constructor
# e2=Employee()#constructor
# e1.display()
# print(e2)
# print(e1)

# write a program to create student class and print object reference
# class Student:
#     name='abcd'
#     email='12@gmail.com'
#     def display(abc):
#         print(abc.name)
#         print(abc.email)
# s1=Student()
# s1.display()
# print(s1)
# take a 2 variables as first name and last name and display the values with the help of function
# class Student:
#     def __init__(self,lname,fname):
#         self.lname=lname
#         self.fname=fname
#     def name(self):
#         print(f'first name:{self.fname}')
#         print(f'last name:{self.lname}')
# s1=Student("abc","xyz")
# s1.name()

# implement multiuser environment with the help of constructor and display the values
# class car:
#     def __init__(self,model,year):
#         self.model=model
#         self.year=year
#
#     def __str__(self):
#         return self.model+self.year
#
#     def display(self):
#         print(f'model:{self.model}')
#         print(f'year:{self.year}')
# c1=car("sedan",2024)
# c2=car("suv",2022)
#
# c1.display()
# c2.display()

#simulate predefined str method to return a string which is containing lname and fname
#concept of overriding
# class Student:
#     def __init__(self,lname,fname):
#         self.lname=lname
#         self.fname=fname
#     def __str__(self):
#         return self.fname+self.lname
#     def name(self):
#         print(f'first name:{self.fname}')
#         print(f'last name:{self.lname}')
# s1=Student("abc","xyz")
# del s1.name
#  s1.name()
#  print(s1)

# class RandmomNumber:
#     x=10
#     def display(self):
#         global x
#         x=8
#         print(x)
#     print(x)
# s1=RandmomNumber()
# s1.display()

#write a program to simulate library management system with the help of class and object,basics data types dictionary .Design and implement library management system the systems should
#allow librarians and users to manage books and respective records
#1.create a function as add book remove book then search book and display list of books present in a library
#
class Library:
    library = {}
    def __init__(self,bookname,authorname):
        self.bookname=bookname
        self.authorname=authorname


    def add_books(self,bookname,authorname):
        self.bookname=input('enter book name')
        if self.bookname in self.library:
            print('book exists')
        else:
            self.authorname=input('enter the author name')
            self.library[self.bookname]=self.authorname
            print(f'{self.bookname} added')

    def search_book(self,bookname):
        self.bookname = input('Enter book name').strip()
        if self.bookname in self.library:
            print(f'{self.bookname}:{self.library[self.bookname]}')
        else:
            print('no book found ')

    def delete_books(self,bookname):
        self.bookname = input('Enter name').strip()

        if self.bookname in self.library:
            del self.library[self.bookname]
            print(f'contact{self.bookname} successfully deleted')
        else:
            print('no contact ')

    def list_books(self):
        if not self.library:
            print('library is empty')
        else:
            print('All books name:')
            for self.bookname, self.authorname in self.library.items():
                print(f'{self.bookname}:{self.authorname}')

    def main(self):
        while True:
            print("1.Add books\n2.Remove books\n3.Search books\n4.list of books")
            choice=input('choose any option').strip()
            if choice=='1':
                self.add_books()
            elif choice=='2':
                self.search_books()
            elif choice=='3':
                self.delete_books()
            elif choice=='4':
                self.list_books()
                # break
            else:
                print('invalid choice')



#############################################################################################################################
# write a program to manage users of library ny creating user id ,username,user contact as data members where add user ,search user, list of users are function members based on end user details
#and requirements create user management system .
#note:to store the data use a dictionary called as user

# class Students:
#     def __init__(self,regno,name,email):
#         self.regno=regno
#         self.name=name
#         self.email=email
#     def display(self):
#         print(self.regno)
#         print(self.name)
#         print(self.email)
# class ma

class Library:
    library = {}
    def __init__(self,bookname,authorname):
        self.bookname=bookname
        self.authorname=authorname


    def add_books(self,bookname,authorname):

        if self.bookname in self.library:
            print('book exists')
        else:

            self.library[self.bookname]=self.authorname
            print(f'{self.bookname} added')

    def search_book(self,bookname):

        if self.bookname in self.library:
            print(f'{self.bookname}:{self.library[self.bookname]}')
        else:
            print('no book found ')

    def delete_books(self,bookname):


        if self.bookname in self.library:
            del self.library[self.bookname]
            print(f'book{self.bookname} successfully deleted')
        else:
            print('no book ')

    def list_books(self):
        if not self.library:
            print('library is empty')
        else:
            print('All books name: authorname')
            for self.bookname, self.authorname in self.library.items():
                print(f'{self.bookname}:{self.authorname}')

    def main(self):
        # bookname=input("enter the book name").strip()
        # authorname=input("enter the author name").strip()
        # l1=Library(bookname,authorname)


        while True:
            print("1.Add books\n2.Remove books\n3.Search books\n4.list of books")
            choice=input('choose any option').strip()
            if choice=='1':
                self.bookname = input("enter the book name").strip()
                self.authorname = input("enter the author name").strip()
                self.add_books(bookname,authorname)


            elif choice=='2':
                self.bookname = input("enter the book name").strip()

                self.search_books(bookname)

            elif choice=='3':
                self.bookname = input("enter the book name").strip()

                self.delete_books(bookname)

            elif choice=='4':
                self.list_books()
                self.library
                break
            else:
                print('invalid choice')

# bookname=input("enter the book name").strip()
# authorname=input("enter the author name").strip()
bookname=""
authorname=""
l1=Library(bookname,authorname)
l1.main()

class Book:
    def __init__(self,book_title,author,ISBN,availability):
        self.book_title = book_title
        self.author = author
        self.ISBN = ISBN
        self.availability = availability
    def displayBook(self):
        return self.book_title,self.author,self.ISBN,self.availability
    
class User:
    def __init__(self,user_id,borrowed_book,returned_book):
        self.userID = user_id
        self.borrowedBook = borrowed_book
        self.returnedBook = returned_book
    def displayUserInfo(self):
        return self.userID , self.borrowedBook,self.returnedBook
    
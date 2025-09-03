class Author:
    def __init__(self,author):
        self.author = author

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    
    def get_info(self):
        return f"Book: {self.title}, Author: {self.author.author}"
    
    
a = Author("Alisher Navoiy")
b = Book("Xamsa", a)
print(b.get_info())
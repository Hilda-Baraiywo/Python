# Base class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
    
    def read(self):
        print(f"Reading '{self.title}' by {self.author}... 📖")
    
    def get_info(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages, Genre: {self.genre}"


# Inheritance
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size):
        super().__init__(title, author, pages, genre)
        self.file_size = file_size
    
    def download(self):
        print(f"Downloading '{self.title}' ({self.file_size}MB)... ⬇️")
    
    # Polymorphism
    def read(self):
        print(f"Reading '{self.title}' on an e-reader... 💻")


# Derived class
class AudioBook(Book):
    def __init__(self, title, author, pages, genre, narrator):
        super().__init__(title, author, pages, genre)
        self.narrator = narrator
    
    def listen(self):
        print(f"Listening to '{self.title}' narrated by {self.narrator}... 🎧")
    
    # Polymorphism
    def read(self):
        print(f"Listening instead of reading '{self.title}'... 🔊")

# Example usage
book1 = Book("1984", "George Orwell", 328, "Dystopian")
ebook1 = EBook("Python Crash Course", "Eric Matthes", 544, "Programming", 5)
audiobook1 = AudioBook("Becoming", "Michelle Obama", 426, "Memoir", "Michelle Obama")

print(book1.get_info())
book1.read()

print(ebook1.get_info())
ebook1.download()
ebook1.read()

print(audiobook1.get_info())
audiobook1.listen()
audiobook1.read()
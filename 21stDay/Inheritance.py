# Inheritance in OOPs

class Writer :
    def __init__(self):
        self.age = 20

    def writing(self) :
        print("He is writing!")    

class Reader(Writer) :
    def __init__(self):
        super().__init__()

    def writing(self): # To add some more functionality in inherited function
        super().writing()
        print("He also read the book!")    

reader = Reader()
print(reader.age)
reader.writing()                
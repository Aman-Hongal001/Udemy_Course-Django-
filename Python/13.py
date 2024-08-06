class Animal():
    def __init__(self):
        print("Animal Created")
    
    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")
    
#inheriting class Animal in Dog
class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self) #initalizing Animal class
        print("Dog Created")
    
    def bark(self):
        print("Woof--bhaw bhaw")
    
    def eat(self):
        print("Dog eating")


# mya = Animal()
mya = Dog()
mya.whoAmI()
mya.eat()
mya.bark()

class Book():
    
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    #special method used to print string when a class object is printed
    def __str__(self):
        return "Title : {}, Author : {}, Pages : {}".format(self.title,self.author,self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("a book is destroyed")

b = Book("Python","Jose",200)
print(b)
print(len(b))
# to delete an object 
del b
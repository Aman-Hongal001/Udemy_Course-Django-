class Dog():
    #Class Object Attribute
    species = "mammal"
    
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
    
#object of class Dog
mydog = Dog("Lab","Sammy")
print(type(mydog))
print(mydog.breed)
print(mydog.name)
print(mydog.species)

class Circle():
    
    pi = 3.14
    #if radius is not provided it will take value as 1
    def __init__(self,radius=1):
        self.radius = radius
    
    def area(self):
        return self.radius*self.radius*Circle.pi
    
    def set_radius(self,new_r):
        self.radius = new_r

myc = Circle(3)
print(myc.radius)
myc.set_radius(10)
print(myc.area())
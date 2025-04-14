#Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
#Add attributes and methods to bring the class to life!
#Use constructors to initialize each object with unique values.
#Add an inheritance layer to explore polymorphism or encapsulation.

#definition of parent class
class sneakers:
    def __init__(self, brand, colour,size):#contructor to initialise attributes with unique values
        self.brand = brand
        self.colour = colour
        self.size = size
    
    #defining methods
    def __str__(self):
        return f"{self.brand}{self.colour}({self.size})"
    
    def displayDetails(self):
        print(self.brand, self.colour, "UK:", self.size)

    def shoesize(self): #this function displays encapsulation
        if self.size > 6:
            print("Your feet are to big for a girl")
        else:
            print("You're probably short")
    

    def clean(self):
        print("Are they clean?")

#definition of derived class
class nike(sneakers): #inheritance: 'nike' inherits propeties and methods from 'sneakers'
    def __init__(self, brand, colour,size): #constructor
        super().__init__(brand,colour,size)
    
    #polymorphism
    def clean(self): 
        print("Nike's are clean!") #overrides functionality of 'clean' from parent class

#definition of derived class
class adidas(sneakers): 
    def __init__(self, brand, colour, size):#constructor
        super().__init__(brand,colour,size)

    def clean(self):
        print("adidas are not clean. Need to be washed")
    

#creating objects of type nike and adidas
N = nike("Nike ", "Red ", 5)
A = adidas("Adidas ", "Black ", 8)

N.displayDetails()
print(N)
N.clean()
N.shoesize()
A.displayDetails()
print(A)
A.clean()
A.shoesize()

print("done!")
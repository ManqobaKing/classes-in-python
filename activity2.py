#polymorphsim
#Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        pass

class car(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        
    def move(self):
        print("Drive!")
        
class boat(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
    
    def move(self):
        print("Sail!")

class plane(vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        
    def move(self):
        print("Fly!")

#creating objects for each vehicle
c = car("BMW","M3")
b = boat("Ibiza","Touring 20")
p = plane("Boeing", "747")

for x in (c,b,p):
    x.move()
    
# super() = Function used in a child class to call method from a parent class (superclass)
#           Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def something():
        pass

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)          #The method is called here with super() referring to the superclass method
        self.radius = radius

    def something():       #You can also override
        print()

circle = Circle(color="red", filled=False,radius=12)


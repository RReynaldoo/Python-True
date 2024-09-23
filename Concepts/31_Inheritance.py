# Inheritance = Allows a class to inherit attributes and methods from another class
#               Help with code reusability
#               Class Child(Parent)

def main():
    dog1 = Dog("Bruce")
    dog1.eat()
    dog1.sleep()
    dog1.speak()

#------------------------------------------------------------------------------------------
class Animal:
    def __init__(self,name,):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")
        
#-------------------------------------------------------------------------------------------
class Dog(Animal):      #Put in parentheses the class this is inheriting from, and can use more than one
    def speak(self):
        print(f"{self.name} barks")     
        
#------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()
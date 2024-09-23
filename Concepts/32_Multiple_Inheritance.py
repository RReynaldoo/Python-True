# multiple inheritance = inherit from more than one parent class
#                        C(a,b)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal:
    def __init__(self,name):
        self.name = name
        
#--------------------------------------------------------------------------
class Prey(Animal):     #inherits from Animal
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):   #inherits from Animal
    def hunt(self):
        print(f"{self.name} is hunting")
        
#--------------------------------------------------------------------------
class Fish(Prey,Predator):  #Inherits form two classes
    pass

#--------------------------------------------------------------------------
def main():
    fish1 = Fish("Nemo")    #Can use the constructor of the ANimal class
    fish1.hunt()            #Hunt as a hunter class
    fish1.flee()            #And flee as a prey class
    
if __name__ == "__main__":
    main()
    
#--------------------------------------------------------------------------

# object = A "bundle" of related attributes (variables) and methods (functions)
#          You need a "class to create many objects

# class = (Blueprint) used to design the structure and layout of an object


def main():
    car1 = Car("Ford",2022,"Green",True)        #To create objects like this
    print(car1.color)   #To access attributes
    car1.drive()        #To use the class methods




class Car:
    def __init__(self, model, year, color, for_sale):     #Constructor of objects
        self.model = model
        self.year = year
        self.color = color
        self.forSale = for_sale
#______________________________________________________
    def drive(self):        #Method/Function
        print(f"You are driving the {self.model}")
    def stop(self):         #Method/Function
        print(f"You stopped the {self.model}")
#-------------------------------------------------------
        
        
        
        
########################################################################################################################
if __name__ == "__main__":
    main()
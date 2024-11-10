class Array(object):

    def __init__(self,capacity,fillValue = None):
        self.items = list()     #Declares items as a list
        for count in range(capacity):   #Appends Nones in the list "items"
            self.items.append(fillValue)

    def __len__(self):
        return len(self.items)      #Gets the length of the list "items"

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def getitem(self,index):
        return self.items[index]

    def __setitem__(self,index,newItem):
        self.items[index] = newItem

def main():
    a = Array(5)
    print(len(a))
    print(a)
    for i in range(len(a)):
        a[i] = i**2
    print(a)
    for item in a:
        print(item)

if __name__ == "__main__":
    main()


#When you do something like object.variable:
#   You are creating a variable for that kind of objects.
#   The can be also another object like list() here in the contructor. Where is the only attribute
#   And is modified by each object using self.intems to change the values of it in each individual object
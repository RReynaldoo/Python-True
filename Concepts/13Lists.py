#Collection = single "variable" used to store multiple values
#List (array like)

#List = []  ordered     changeable      Duplicates Yes      modifiable
#Set  = {}  unordered   immutable       Duplicates No       Add/Remove
#Tuple= ()  ordered     unchangeable    Duplicates Yes                      Fast

fruit = ["banana", "orange", "coconut"]

fruit[1] = "Nothingness"                #Can add like normally would
fruit[1] ,fruit[0:2], fruit[::-1]       #Can iterate through them as with range and indexes in strings

len(fruit)                  #For the length of the list
dir(fruit) / help(fruit)    #shows useful stuff
fruit.append()              #Adds an element at the end of a list
fruit.remove()              #Removes an element from the list
fruit.insert(1,"Apple")     #Inserts something in a position
fruit.sort()                 #Sorts in alphabetical, or number depending on the datatype
fruit.reverse()              
fruit.clear()
fruit.index("banana")        #Returns the index of an item in the list
fruit.count("banana")        #Returns the number of times this item is repeated
fruit.pop()                  #Removes the last item of the list (Otherwise you can specify the position)
("banana" in fruit )         #Checks if an element exists

#Whe you use negative indexes, it will give you the values in inverted order
i[-1]   #Last element
i[-2]   #Before last element
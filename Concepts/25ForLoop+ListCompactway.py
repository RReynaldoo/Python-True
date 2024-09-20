# List comprehension =  A short/fast way to create lists
#                       Compact and easier to read than tradicional loops
#                       ["expression" for "value" in "iterable" if "condition"]
#expresion and value use same variable and the expresion is where we modify the value returned, if left untouched it will be assign to the list as is



doubles = [x*2 for x in range(1,11)] #Fills the list with the numbers [2,4,6,8,10,12,14,16,18,20]

letters = ["one","two","three","four","five"]
upperCase = [i.upper() for i in letters]            #Stores all elements of the list in uppercase
first_letter = [i[0] for i in letters]              #Stores all first letters of elelments in the list

numbers = [1,2,-3,-4,5,-6]
positives = [num for num in numbers if num>=0]      #Stores all positive numbers


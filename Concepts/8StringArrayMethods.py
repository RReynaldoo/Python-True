some = "hola"

some += "hi"        #Adds this to the string
some.len()          #Returns the length of a string             Returns integer
some.find()         #Finds the first occurrence of a character  Returns a string        -1 if it doesn't find anything
some.rfind()        #Finds the last occurrence of a character   Returns a string
some.capitalize()   #Uppercase the first letter of the string

#Used with strings and arrays like: my_lyst.upper() to CAPITALIZE all elements 
some.upper()
some.lower()

some.isdigit()
some.isalpha()      #Checks if the string is only alphabetical characters
some.count()        #Counts how many occurrences of a character there are in a string
some.replace(x,y)   #Replaces all occurrences of a string character with another
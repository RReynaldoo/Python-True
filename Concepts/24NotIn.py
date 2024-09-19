#membership operators = used to test whether a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                        in / not in

#EXAMPLE WITH STRING
my_string = "FLORIDA"

my_boolean = "O" in my_string
print(my_boolean)

my_boolean = "Z" not in my_string
print(my_boolean)

#-----------------------------------------------------------------------------------------------
#EXAMPLE WITH DICTIONARY

my_dictionary = {"Alex":100,"Michael":98,"Richard":88}

guess = Alex

if guess in my_dictionary:
    print(f"The student {guess} has average grades of {my_dictionary[guess]}")
else:
    print("Student no found")

#----------------------------------------------------------------------------------------------
#EXAMPLE WITH LIST
my_list =[1,2,3,4,5,6]

if 1 and 6 in my_list:
    print("Yessir")
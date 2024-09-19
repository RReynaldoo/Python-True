# keyword arguments = arguments prefixed with the names of parameters
#                                        order of the arguments doesn’t matter
#                                        helps with readability

# ----- EXAMPLE 1 -----
def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", title="Mr.", last="John", first="James")     #You assign the values calling the parameters so it helps with readability and makes it easier to handle

# ----- EXAMPLE 2 -----
for number in range(1, 11):
    print(number, end=" ")                  
print("1", "2", "3", "4", "5", sep="-")     #End and sep are great examples of this function in action
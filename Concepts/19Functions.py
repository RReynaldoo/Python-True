#function = A block of reusable code
#           place () after the function name to invoke it

def happy_birthday(name,age):           #Because it does not specify the datatype we have to be careful with the order of the data we send to them
    print(f"Happy birthday to {name}")
    print(f"You are {age} old")
    print(f"Happy birthday to {name}")
    print()

happy_birthday("Nick", 12)

#---------------------------------------------------
#return =   statement used to end a function
#           and send a result black to the caller

def add(x,y):
    z = x+y
    return z

print(add(2,3))

# If there is no return, then it will return None
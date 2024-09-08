# *args     =   allows to pass multiple non-key arguments   (creates a tuple in the function, so treat it as such)
# **kwargs  =   allows to pass multiple keyword-arguments   (Creates a dictionary called kwargs, so treat it as such)
#           * unpacking operator
#           position/default/keyword/ARBITRARY

#ARGS
#-----------------------------
def add(*args):                   #Receives all the arguments and stores them in the tuple "args"
    result = 0
    for i in args:
        result += i
    return result

print(add(1,2,3,4,5))       #Sends all these arguments to a tuple in the function
#-----------------------------

#KWARGS
#-----------------------------
def address(**kwargs):              #Receives all the arguments and stores them in the dictionary called "kwargs"
    for i in kwargs.values():
        print(i)

address(street="Monroe",city="Elizabeth",state="New Jersey")    #Sends all the values to the function as a dictionary
#-----------------------------





#ARGS, KWARGS
#-------------------------------------------
def something(*args,**kwargs):          #You can have both in a function. Remember that here they behave like tuples and dictionaries, so treat them as such
    result = 0
    for i in args:
        result += i
    return result

    for i in kwargs.values():
        print(i)
#------------------------------------------
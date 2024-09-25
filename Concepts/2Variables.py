#Variables = no need to specify the data type, just assign them

a = 12          #Integers

b = 12.99       #floats

c = True        #booleans
c = bool(string)#True if there is something in, False if not

d = "anything"  #strings

a,d = d,a       #To swap the values of variables

#----------------------------------------------------------------------------------------------------------------
#They can change at any time, so if you stored a str it can also be a int if you assign it

#There are no means to create constants, so you can only indicate they are so by using UPPER_CASE to indicate it\
#----------------------------------------------------------------------------------------------------------------


>>> true_variable = True and True
>>> false_variable = True and False

>>> true_variable = False or True               #Useful patterns to evaluate several statements using conventional (p > ~q) patterns
>>> false_variable = False or False

>>> true_variable = not False
>>> false_variable = not True
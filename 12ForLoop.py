# for loops =   execute a block of code a fixed number of times
#               You can iterate over a range,string,sequence,etc
name = "James"

for i in range(1,12, 2):        #This prints numbers in a given range, from 1 to 12 skipping 2
    print(i)                    #If left empty then it won't skip by any
    
for i in reversed(range(1,12,2)):       #Use reversed function to count backwards. like -1 in java
    print(i)
    
for i in name:                  #Can use any of the other datatypes
    print(i)
    
    
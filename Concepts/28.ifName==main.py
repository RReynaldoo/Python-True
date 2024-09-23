# if __name__ == __main__: 

# If this is in a file this means that the code that is enclose in there will only be executed if the file is executed
# Otherwise it will not execute the code

#This is usefull because it means that the file can be imported or used stand alone
# So if it has useful funtions we can use it and not execute the code in there, unless the file is executed directly

def get_power(a,b):
    b = a ** b
    print(b)


################This is only executed if the file is executed, otherwise, if imported, it wont run
def main():
    a = int(input())
    b = int(input())
    get_power(a,b)

if __name__ == '__main__':
    main()
###################################################################################################
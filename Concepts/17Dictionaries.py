#dictionaries = a collection of {key: value} pairs
#               ordered and changeable. No duplicates

#In dictionaries, the index is not a number, the key is
"""
##########  Instead of     users_passwords[0]     ##########
##########  You would use  users_passwords[Adam]  ##########
"""

users_passwords = { "Adam":"Lastdance1324%",
                    "Tobias":"contrasena1324",
                    "Gena":"Tokyoghetto1324%00"
                  }

users_passwords.get("adam")                                 #To get the value of a key / if not found will return "none", which is useful with "if else" or boolean operations
users_passwords.update({"Louise": "amoamifamilia1324"})     #To change or add a new {key: value} to the dictionary
users_passwords.pop("Tobias")                               #To delete a {key: value}
users_passwords.popitem()                                   #To delete the latest {key: value} of the dictionary
users_passwords.clear()                                     
users_passwords.keys()                          #Returns the keys of the dictionary 
users_passwords.values()                        #Returns the values of the dictionary
users_passwords.items()                         #Returns the {key: value} of the dictionary

    #--------------To show all the values of the dictionary------------------
    for key, value in users_passwords.items()   #Use two variables next to "for" because there are two elements next to each other in a dictionary rather than one
        print(f"{key}:{value}")

    for a in users_passwords.keys():    #Iterate only through keys
    print(a)

    for b in users_passwords.values():  #Iterate only through keys
    print(b)

    #------------------------------------------------------------------------
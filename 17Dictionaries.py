#dictionaries = a collection of {key: value} pairs
#               ordered and changeable. No duplicates

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
    for key, value in kwargs.items()
        print(f"{key}:{value}")
    #------------------------------------------------------------------------
#Indexing with strings = access elements in a sequence of a string using []
#                            [start : end : step]
#

name = "josh"

print(name[1])      #displayes the index given
name[1:3]           #displays from an index to another
name[1:2:3]         #Displays form an index to another in steps
name[::3]           #displays all in steps || adding a start or end will make it end or start there
name[::-1]          #displays all backwards|| with limits it will have an end

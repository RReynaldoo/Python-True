#Match-case statement (switch): An alternative to using many "Elif" statements
#                               Execute some code if value matches a case
#                               Cleaner syntax and more readable

def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday"|"Thursday" | "Friday":      #You can stack conditions like this
            print("It is not weekend")
        case "Saturday" | "Sunday":
            print("Yes it is")
        case _:                                                              #Use _ at the end for default
            print("It is not weekend")

is_weekend(day = input(str()))
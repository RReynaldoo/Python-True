# format specifiers = {:flags} format a value based on what flags are inserted

#.(number)f = round to that many decimal places
# (number) = allocate that many spaces and puts the quantity in the end in the amount of 0 that they use
# 0(number) = allocate and zero pad that many spaces
# < = left justify
# > = right justify
# ^ = center align
# + = use a plus sign to indicate positive value
# = = place sign to leftmost position
#   = insert a space before positive numbers
# , = comma separator
# % = percentage format

price1 = 3.14159
price2 = -987.65
price3 = 12.34
print(f"price1 is: ${price1:0}")
print(f"price2 is: ${price2: }")
print(f"price3 is: ${price3: }")

#you can conbime them putting them next to one another.
#You can always add a number with anyone to state the number of spaces you want

###############################################################
#A second way, a little less readable is:

print("%[flags][width][.precision]type" % value)
print("%10s%20s" % ("Problem Size","Seconds"))

# %: Indicates a placeholder for a value.
# [flags]: Optional flags that can be used to modify the output. 
# [width]: The minimum field width for the value.
# [.precision]: The maximum number of digits to display for floating-point numbers.
# type: The type of value to be inserted. Common types include:

# s: string
# d: decimal integer
# f: floating-point number
# x: hexadecimal integer
# value: The value to be inserted into the string.

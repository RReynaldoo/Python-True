# default arguments =   A default value for certain parameters
#                       default us used when that argument is omitted
#                       make your functions more flexible, reduces # of arguments
#                       positional/DEFAULT/keyword/arbitrary

def net_price(list_price,discount=0,tax=0.05):      #DEFAULT    = if no value is passed for parameters with a value assign then they will use the assign one
    return list_price * (1 - discount) * (1 - tax)


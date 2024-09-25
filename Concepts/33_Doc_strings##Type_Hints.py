# Docstrings = are used to document modules, functions, classes and methods
#              They can be accessed programmatically at runtime using the __doc__ attribute


def greet(name: str) -> None:       #"-> None" is a type hint indicating that a function returns no value
                                    # It doesn't affect the functionality of the function
                                    # Same applies for  ": str" which implies that name should be a string but you can still pass a int, for instance

    """Print a personalized greeting message.

    Args:
        name (str): The name of the person to greet.

    Returns:
        None
    """
    print(f"Hello, {name}!")

print(greet.__doc__)    #with name of the function and __doc__ you can see its contents
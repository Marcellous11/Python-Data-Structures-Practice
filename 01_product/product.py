def product(a, b):
    """Return product of a and b.

        >>> product(2, 2)
        4

        >>> product(2, -2)
        -4
    """
    if type(a) != int or type(b) != int:
        print("Enteries must be interagers")
    else:
        return a * b 


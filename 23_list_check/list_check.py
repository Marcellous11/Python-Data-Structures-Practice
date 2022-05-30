def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    my_list = []
    for val in lst:
        if type(val) != list:
            my_list.append(val)
    if len(my_list) > 0:
        return False 
    else:
        return True
    
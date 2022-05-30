def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = []
    for x in phrase:
        if x == to_swap.upper() or x == to_swap.lower():
            if x.islower():
                lst.append(x.upper())
            elif x.isupper():
                lst.append(x.lower())
        else:
            lst.append(x)
    string = ''.join(lst)
    return string
        

            


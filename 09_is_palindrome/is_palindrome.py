def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
      

    start = phrase.lower()
    main_list = list(start)

    for x in main_list:
        if x == " ":
            main_list.remove(x)
        
    list_length = len(main_list)

    if list_length % 2 == 0:
        half_point = int(list_length/2)
        print(half_point)
        first_half = main_list[0:half_point]
        print(first_half)

        second_half = main_list[half_point:]
        second_half.reverse()
        print(second_half)

        return first_half == second_half
    else: 
        list_length % 2 != 0
        half_point = int((list_length/2) +1 )
        print(half_point)
    
        first_half = main_list[0:half_point]
        first_half.pop()
        print(first_half)

        second_half = main_list[half_point:]
        second_half.reverse()
        print(second_half)

        return first_half == second_half
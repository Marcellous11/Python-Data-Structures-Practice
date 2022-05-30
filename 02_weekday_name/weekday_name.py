def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    name_of_the_days = {1: "Sunday",2:"monday",3:"Tuesday",4:"Wednesday",5:"Thursday",6:"Friday",7:"Saturday"}
    if type(day_of_week) == str:
        return None
    elif day_of_week == 0 or day_of_week > 7:
        return None
    else:
        return name_of_the_days[day_of_week]

    
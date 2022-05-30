def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    answer_list = []
    for item in lst:
        if bool(item):
            answer_list.append(item)
    return answer_list
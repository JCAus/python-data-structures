def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    
    for x in lst:
        if x is not True:
            lst.pop(lst.index(x))
    
    print(lst)

compact([0, 1, 2, '', [], False, (), None, 'All done'])
def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    freq = 0
    for num in lst:
        if num == search_term:
            freq += 1
    
    print(freq)

frequency([1, 3, 4, 5, 5, 5, 8], 5)
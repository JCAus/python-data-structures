def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    same_nums = []
    both = set()
    for num in l1:
        for num in l2:
            if num in l1 and l2:
                both.add(num)
    for num in both:
        same_nums.append(num)
    print(same_nums)
intersection([1, 2, 3], [2, 3, 4])

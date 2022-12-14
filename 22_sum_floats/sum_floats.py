def sum_floats(nums):
    """Return sum of floating point numbers in nums.
    
        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9
        
        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!
    floats = []
    for items in nums:
        if isinstance(items, float) is True:
            floats.append(items)
    for num in floats:
        num += num
        print(num)

sum_floats([1.5, 2.4, 'awesome', [], 1])

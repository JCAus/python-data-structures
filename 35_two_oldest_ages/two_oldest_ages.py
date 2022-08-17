def two_oldest_ages(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages([1, 5, 5, 2])
        (2, 5)
    """

    # NOTE: don't worry about an optimized runtime here; it's fine if
    # you have a runtime worse than O(n)

    # NOTE: you can sort lists with lst.sort(), which works in place (mutates);
    # you may find it helpful to research the `sorted(iter)` function, which
    # can take *any* type of list-like-thing, and returns a new, sorted list
    # from it.

    # num_freq = {num: ages.count(num) for num in ages}

    # num_values = num_freq.values()
    # num_keys = num_freq.keys()

    two_oldest = []
    
    oldest = ages.pop(ages.index(max(ages)))
    
    two_oldest.append(oldest)

    for num in ages:
        if num == two_oldest[0]:
            ages.pop(ages.index(num))

    two_oldest.insert(0, max(ages))
    tuple_of_oldest = tuple(two_oldest)
    print(tuple_of_oldest)
two_oldest_ages([6, 1, 9, 10, 4])
two_oldest_ages([1, 5, 5, 2])

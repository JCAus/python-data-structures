def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    every_other = lst[0:len(lst): 2]
    print(every_other)

my_lst = [1, 2, 3, 4, 5]
remove_every_other(my_lst)

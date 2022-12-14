def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    num_dict = {num: nums.count(num) for num in nums}
    
    keys_list = list(num_dict.keys())
    vals_list = list(num_dict.values())

    mode_idx = vals_list.index(max(vals_list))

    
    print(keys_list[mode_idx])

mode([1, 2, 1, 3, 3, 3, 3])
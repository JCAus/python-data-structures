def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    sum_pair = []
    for num in nums:
        future_nums = nums[nums.index(num) + 1:len(nums):1]
        for number in future_nums:
            if num + number == goal:
                sum_pair.append(num)
                sum_pair.append(number)
        if len(sum_pair) == 2:
            print(tuple(sum_pair))
    
                
           


sum_pairs([5, 1, 4, 8, 3, 2], 7)
sum_pairs([1, 2, 2, 10], 4)
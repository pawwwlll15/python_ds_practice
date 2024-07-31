def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """
    counter = 1
    greater_num_total = 0
    
    for num in nums:
        #splicing list each time to avoid starting from beginning of nums
        num_range = nums[counter:len(nums)]
        for number in num_range:
            if num < number:
                greater_num_total += 1
        
            
        
        counter += 1


    

    return greater_num_total
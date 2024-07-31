def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    #sort to get matching numbers next to each other
    nums.sort()
    #using i allows me to access index points in list. 
    #if num is equal to next num, we have a matching pair! return that number
    for i in range(len(nums) -1):
        num = nums[i]
        next_num = nums[i +1]

        if num == next_num:
            return num
    #else return None
    return None
        
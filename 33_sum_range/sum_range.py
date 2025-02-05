
nums = [1, 2, 3, 4]

def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum_result = 0
    if end != None and end > len(nums):
        end = len(nums) - 1
        
    if start == 0 and end == None:
        for num in nums:
            sum_result += num
    elif start > 0 and end == None:
        nums = list(range(start + 1,len(nums) + 1))
        for num in nums:
            sum_result += num
    elif start >= 0 and isinstance(end,int):
        nums = list(range(start + 1, end + 2))
        for num in nums:
            sum_result += num
  

    return sum_result
    
    
            

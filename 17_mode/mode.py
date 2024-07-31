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
    dictionary = {}
    for num in nums:
        dictionary[num] = dictionary.get(num,0) + 1
    
    max_value = max(dictionary.values())
    #key_with_highest_value = for each key in dictionary items, check its value, if its value is equal to max_value, add it to this list 
    key_with_highest_value = [key for key, value in dictionary.items() if value == max_value]

    return key_with_highest_value[0]
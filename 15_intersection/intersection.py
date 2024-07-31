def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    #intersection is the element that appears in both lists
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    intersectors = []
    for num1 in l1:
        for num2 in l2:
            if num1 == num2:
                intersectors.append(num1)
    
    return intersectors
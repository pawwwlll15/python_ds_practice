
def is_even(num):
    return num % 2 == 0
    
def is_string(el):
    return isinstance(el, str)


def partition(lst, fn):
    """Partition lst by predicate.
     
     - lst: list of items
     - fn: function that returns True or False
     
     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0
        
        >>> def is_string(el):
        ...     return isinstance(el, str)
        
        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]
        
        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """
    
    if fn is is_even:
        even = []
        odd = []
        return_list = [even,odd]
        for num in lst:
            if is_even(num):
                even.append(num)
            else:
                odd.append(num)
        
    
    elif fn is is_string:
        strings = []
        not_strings = []
        return_list = [strings,not_strings]
        for item in lst:
            if is_string(item):
                strings.append(item)
            else:
                not_strings.append(item)
    
    return return_list

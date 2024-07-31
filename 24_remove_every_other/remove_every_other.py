def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    every_other = []
    counter = 0
    for num in lst:
        counter += 1
        if counter % 2 != 0:
            every_other.append(num)
    
    return every_other

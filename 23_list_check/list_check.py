def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
    test_list = []
    for item in lst:
        if isinstance(item,list):
            test_list.append(item)
    if len(test_list) == len(lst):
        return True
    else:
        return False
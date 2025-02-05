def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

#adding items to lists
    if command == 'add' and location == 'end':
        #append adds at end of list
        lst.append(value)
        return lst
    elif command == 'add' and location == 'beginning':
        #insert allows you to add anywhere in list
        lst.insert(0,value)
        return lst

#removing items from lists
    if command == 'remove' and location == 'end':
        lst.pop()
        return lst
    elif command == 'remove' and location == 'beginning':
        lst.pop(0)
        return lst
    
#handling invalid commands
    if command != 'remove' or command != 'add':
        return None
    elif location != 'beginning' or location != 'end':
        return None
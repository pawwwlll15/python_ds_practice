def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    string_num1 = str(num1)
    string_num2 = str(num2)

    if len(string_num1) == len(string_num2):
        return True
    else:
        return False
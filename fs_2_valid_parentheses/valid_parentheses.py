def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    #create empty dictionary
    parens_dict = {}

    #if first character is ')' return false, because '(' always comes first
    if parens[0] == ')':
        return False
    
    #for each char in parens, assign that char to a key in dictionary.
    #if it exists in dictionary add 1 to value, if not create key and set value to 1
    for char in parens:
        parens_dict[char] = parens_dict.get(char,0) + 1

    #if there are the same amount of "(" as there are ")" then we have valid parnetheses
    if parens_dict['('] == parens_dict[')']:
        return True
    return False
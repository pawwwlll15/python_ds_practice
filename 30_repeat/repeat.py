def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> c
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    counter = 0
    returned_phrase = ''
    if not isinstance(num,int) or num < 0:
        return None
    else:
        while counter < num:
            counter +=1
            returned_phrase += phrase
    return returned_phrase
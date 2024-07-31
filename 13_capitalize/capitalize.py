def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    capitalized = ''
    for char in phrase:
        if len(capitalized) == 0:
            char = char.upper()
            capitalized += char
        else:
            capitalized += char
    return capitalized


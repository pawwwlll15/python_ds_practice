def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ''
    for char in phrase:
        if char == to_swap.lower():
            flipped += char.upper()
        elif char == to_swap.upper():
            flipped += char.lower()
        else:
            flipped += char
    return flipped

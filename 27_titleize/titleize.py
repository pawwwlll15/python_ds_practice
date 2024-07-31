def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    capitalized_phrase = ''
    caps_next = True
    for char in phrase:

        if char == ' ':

            caps_next = True
            capitalized_phrase += char

        elif caps_next or len(capitalized_phrase) == 0:
            capitalized_phrase += char.upper()

            caps_next = False
        
        else:
            capitalized_phrase += char.lower()

    return capitalized_phrase



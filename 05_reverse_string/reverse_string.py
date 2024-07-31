def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #:: is start and end for the 'range'. since both are edmitted it will start at the end and go backwards 1 as it loops through the string
    reversed_string = phrase[::-1]

    return reversed_string    
    
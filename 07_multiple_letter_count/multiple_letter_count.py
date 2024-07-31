def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    dictionary = {}
    for char in phrase:
        # .get allows me to find the char in the dictionary and add 1 to its value. if it doesn not exist, create one and set its value to 1
        dictionary[char] = dictionary.get(char,0) + 1

    return dictionary
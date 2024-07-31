def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    #create string of vowels
    vowels = 'aeiou'
    #string to store taken vowels
    taken_vowels = ''
    #string to store word with replacement char inplace of vowel locations
    spaced_s = ''
    #string with vowels in reversed positions
    reversed_vowels = ''
    #compare each char to each vowel, if char is a vowel, add char to taken_vowels then change that char to '1'
    #add char to spaced_s
    for char in s:
        for v in vowels:
            if char.lower() == v:
                taken_vowels += char
                char = '1'
        
        spaced_s += char
    
    #reverse vowels
    taken_vowels = taken_vowels[::-1]

    #set counter
    counter = 0
    #now go back through spaced_s, if char == '1', change char to vowel at position counter in taken_vowels
    for char in spaced_s:
        if counter < len(taken_vowels):
            if char == '1':
                char = taken_vowels[counter]
                #add counter to get to next vowel in string
                counter += 1
        
        #add char to reversed_vowels
        reversed_vowels += char
    return reversed_vowels




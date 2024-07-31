def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    counter = 0
    total = 0
    #for each list add value of list item at counter index to total
    for lst in matrix:
        total += lst[counter]
        counter += 1

    #reset counter to last index in matrix
    counter -= 1

    #now loop backwords through same list of list's and retrieve item at counter index
    #and add them to total
    for lst in matrix:
        total += lst[counter]
        counter -= 1

    
    
    return total
        

   

    
    
    


"""  
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = [[1,   2],[30, 40]]

sum1 = lst_1[0] + lst_2[1]
sum2 = lst_1[1] + lst_2[0] 

"""
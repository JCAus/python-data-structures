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
    total = 0
    for lst in matrix:
        for i in range(0, len(matrix)):
            total += lst[matrix.index(matrix[i])]
    
            total += lst[len(matrix) - 1 - matrix.index(matrix[i])]
    answer = total / len(matrix)
    print(answer)

m2 = [[1, 2, 3, 4], 
      [5, 6, 7, 8], 
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
sum_up_diagonals(m2)
def zero_matrix(matrix):
    """
    sets row and column to 0 if an element is 0
    """
    # 1. find all rows and columns that have a 0
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)

    # 2. set all elements in those rows and columns to 0
    for row in rows:
        for j in range(len(matrix[0])):
            matrix[row][j] = 0

    for col in cols:
        for i in range(len(matrix)):
            matrix[i][col] = 0
    
    
    return matrix
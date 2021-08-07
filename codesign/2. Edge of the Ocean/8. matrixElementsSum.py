def matrixElementsSum(matrix):

    cost = 0

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x > 0:
                if matrix[x-1][y] == 0:
                    matrix[x][y] = 0
            cost += matrix[x][y]
    return cost

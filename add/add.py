def add(matrix1, matrix2):
    matrixsum = []     
    for i in range(len(matrix1)):
        sublist = []
        for j in range(len(matrix1[i])):
            sublist.append(matrix1[i][j] + matrix2[i][j])
        matrixsum.append(sublist)
    return matrixsum
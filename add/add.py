def getMatrixSize(matrix):
    return [len(r) for r in matrix]

def add(*matrices):
    firstMatrixSize = getMatrixSize(matrices[0])
    if any(getMatrixSize(m) != firstMatrixSize for m in matrices):
        raise ValueError("All matrices are not the same size.")
    return [ 
        [sum(values) for values in zip(*rows)] 
        for rows in zip(*matrices)
    ]
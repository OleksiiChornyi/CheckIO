from typing import List

def checkio(matrix: List[List[int]]) -> bool:
    #replace this for solution
    size = len(matrix)
    for i in range(0, size):
        for j in range(0,size-3):
            if (matrix[i][j] == matrix[i][j+1]
                and matrix[i][j] == matrix[i][j+2]
                and matrix[i][j] == matrix[i][j+3]):
                return True
    for i in range(0, size-3):
        for j in range(0,size):
            if (matrix[i][j] == matrix[i+1][j]
                and matrix[i][j] == matrix[i+2][j]
                and matrix[i][j] == matrix[i+3][j]):
                return True   
    for i in range(0, size-3):
        for j in range(0,size-3):
            if (matrix[i][j] == matrix[i+1][j+1]
                and matrix[i][j] == matrix[i+2][j+2]
                and matrix[i][j] == matrix[i+3][j+3]):
                return True
    for i in range(3, size):
        for j in range(0,size-3):
            if (matrix[i][j] == matrix[i-1][j+1]
                and matrix[i][j] == matrix[i-2][j+2]
                and matrix[i][j] == matrix[i-3][j+3]):
                return True       
    return False

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')


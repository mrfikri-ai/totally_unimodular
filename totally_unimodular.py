import numpy as np
import sys
import itertools

'''
Totally Unimodular has several properties. In this code, we would like to give a proof
matrix A is totally unimodular
1. Matrix is totally unimodular if any submatrix of A has determinant -1, 0, 1
2. Transpose of A is also totally unimodular if matrix A is Totally unimodular
'''

def checkRule1(A):
    '''Check if every element in A is 0, 1, or -1'''
    for i in np.nditer(A):
        if i not in [-1, 0, 1]:
            return False
    return True

def checkRule2(A, r, c):
    '''Check if a submatrix has a determinant of 0, 1, or -1'''
    det = A[r[0], c[0]] * A[r[1], c[1]] - A[r[0], c[1]] * A[r[1], c[0]]
    return det in [-1, 0, 1]

def theoremSeymour(A):
    '''
    Check Rule 1 for matrix A
    Generate all 2x2 submatrices of A and check Rule 2
    Check Seymour's Theorem: If all the 2x2 submatrices of A satisfy Rule 2, then A is totally unimodular.
    '''
    if checkRule1(A):
        n, m = A.shape
        rows = list(itertools.permutations(range(n), 2))
        cols = list(itertools.permutations(range(m), 2))
        for r in rows:
            for c in cols:
                if not checkRule2(A, r, c):
                    return False
        return True
    return False

def transposeMatrix(A):
    '''Return the transpose of matrix A'''
    return np.transpose(A)


if __name__ == '__main__':
    A = np.array([[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,],
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,],
                [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,],
                [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,], 
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,],   
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,]])


    A_transpose = transposeMatrix(A)
    print('Transposed matrix A:')
    # print(A_transpose)

    if theoremSeymour(A_transpose):
        print('A is a totally unimodular matrix according to Seymour\'s Theorem')
    else:
        print('A is not a totally unimodular matrix according to Seymour\'s Theorem')

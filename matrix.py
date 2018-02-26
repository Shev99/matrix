import math 

def print_matrix( matrix ):
    for row in matrix:
        for col in row:
            print col, " ",
        print " "
    print "\n"


def ident(matrix):
    for i in range(4):
        matrix[i][i] = 1

def new_matrix(rows = 4, cols = 4):
    matrix = []
    for c in range(cols):
        matrix.append([])
        for r in range(rows):
            matrix[c].append(0)
    return matrix

def matrix_mult(m1,m2):
    tempAns = new_matrix(len(m2[0]),len(m2))
    for row1 in range(len(m1)):
        for col2 in range(len(m2[0])):
            for row2 in range(len(m2)):
                tempAns[row1][col2] += m1[row1][row2] * m2[row2][col2]
    #copy:
    for r in range(len(tempAns)):
        for c in range(len(tempAns[0])):
            m2[r][c] = tempAns[r][c]


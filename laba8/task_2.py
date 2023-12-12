from random import randint

def matrix(n = randint(2,4), m = randint(2,4)): # фунция создания матрицы
    return [[randint(-9,99) for j in range(m)] for i in range(n)]

def print_matrix(matrix): # функция вывода матрицы
    for i in range(len(matrix)):
        print(*matrix[i])
    print()

def MaxElemMatrix(matrix): # фунция поиска максимального элемента в матрице
    MaxElem = matrix[0][0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if MaxElem < matrix[i][j]:
                MaxElem = matrix[i][j]
    return MaxElem

def ChangeElem(matrix,value_finally): # функция замены максимальных значений одной матрицы на вводимое
    value_past = MaxElemMatrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value_past:
                matrix[i][j] = value_finally

def ChangeMaxElemTwoMatrix(matrix_1, matrix_2): # функция перестановки местами максимальных значений двух матриц
    max_1 = MaxElemMatrix(matrix_1)
    max_2 = MaxElemMatrix(matrix_2)
    ChangeElem(matrix_1,max_2)
    ChangeElem(matrix_2,max_1)


A = matrix()
B = matrix()

print_matrix(A)
print_matrix(B)

ChangeMaxElemTwoMatrix(A,B)

print_matrix(A)
print_matrix(B)
# добавляю еще один коммент для гита
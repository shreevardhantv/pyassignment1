"""
Excercise 10.7

Question 10: Write a menu-driven program to input two matrices and do the following:
(a) Find the sum of the two matrices
(b) Find the difference of the two matrices
(c) Find the product of the two matrices
"""

def input_matrix():
    print("Enter matrix.")
    m = int(input("Enter no. of rows: "))
    n = int(input("Enter no. of columns: "))
    matrix = [[0 for _ in range(m)] for _ in range(n)]

    for y in range(n):
        for x in range(m):
            matrix[y][x] = float(input(f"Enter element {y + 1},{x + 1}: "))

    return matrix

def matrix_sum(a, b):
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        raise ValueError("Input matrixes are not of same size.")
    return [[a[y][x] + b[y][x] for x in range(len(a[0]))] for y in range(len(a))]

def matrix_diff(a, b):
    if (len(a), len(a[0])) != (len(b), len(b[0])):
        raise ValueError("Input matrixes are not of same size.")
    return [[a[y][x] - b[y][x] for x in range(len(a[0]))] for y in range(len(a))]

def matrix_product(a, b):
    result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * a[k][j]
    
    return result

def matrix_print(matrix):
    print("\n".join([" ".join(str(j) for j in matrix[i])for i in range(len(matrix))]))

matA, matB = input_matrix(), input_matrix()

menu = "MENU (Input 1/2/3/4/5)\n1. Sum of the two matrices\n2. Difference of the two matrices\n3.Product of the two matrices\n4. redefine matrices\n5. Exit"
while True:
    opt = int(input(menu))

    match opt:
        case 1:
            matrix_print(matrix_sum(matA,matB))
        case 2:
            matrix_print(matrix_diff(matA, matB))
        case 3:
            matrix_print(matrix_product(matA, matB))
        case 4:
            matA, matB = input_matrix(), input_matrix()
        case 5:
            break
        case _:
            print("Invalid menu option. Try again")
    input("Press Enter to continue")

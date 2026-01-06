# Omer Subasi

def rotate(matrix):
    self.transpose(matrix)
    self.reflect(matrix)

def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

def reflect(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]

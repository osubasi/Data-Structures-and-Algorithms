# Omer Subasi

def searchMatrix(matrix, target):
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    left = 0
    right = m * n - 1 
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        if target == matrix[row][col]:
            return True
        else:
            if target < matrix[row][col]:
                right = mid - 1
            else:
                left = mid + 1
    return False

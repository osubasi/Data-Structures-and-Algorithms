# Omer Subasi

def knightProbability(n, k, row, column):
    prevM = [[1.0] * n for _ in range(n)]
    currM = [[0.0] * n for _ in range(n)] 
    directions = [[1, 2], [2, 1], [-1, 2], [2, -1], [1, -2], [-2, 1], [-1, -2], [-2, -1]]
    for move in range(1, k+1):
        for i in range(n):
            for j in range(n):
                curr = 0.0
                for d in directions:
                    u = i + d[0]
                    v = j + d[1]
                    if 0 <= u < n and 0 <= v < n:
                        curr += prevM[u][v] / 8.0
    
                currM[i][j] = curr
        prevM = [row[:] for row in currM]
    
    return prevM[row][column]

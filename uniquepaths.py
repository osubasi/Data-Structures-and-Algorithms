# Omer Subasi

def uniquePaths(m, n):
    d = [[1 for _ in range(n)] for _ in range(m)]
    for y in range(1, m):
        for x in range(1, n):
            d[y][x] = d[y-1][x] + d[y][x-1]

    return d[m-1][n-1]

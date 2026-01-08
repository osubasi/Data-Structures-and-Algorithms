# Omer Subasi

def longestIncreasingPathMatrix(matrix):
    def dfs(r, c, matrix, memo):
        if memo[r][c] != 0:
            return memo[r][c]
        max_pth = 1
        m = len(matrix)
        n = len(matrix[0])
        for d in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            n_r = r + d[0]
            n_c = c + d[1]
            if (0 <= n_r < m and 0 <= n_c < n and matrix[n_r][n_c] > matrix[r][c]):
                max_pth = max(max_pth, 1 + dfs(n_r, n_c, matrix, memo))
        memo[r][c] = max_pth
        return max_pth

    if not matrix:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    memo = [[0] * n for _ in range(m)]
    res = 0
    for r in range(m):
        for c in range(n):
            res = max(res, dfs(r, c, matrix, memo))
    return res

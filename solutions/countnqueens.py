# Omer Subasi

def countNQueens(n):
    def dfs(r, cols, diags, antidiags, n, res):
        if r == n:
            res += 1
            return res
        for c in range(n):
            diag = r - c
            antidiag = r + c
            if(c in cols or diag in diags or antidiag in antidiags):
                continue
            cols.add(c) 
            diags.add(diag) 
            antidiags.add(antidiag)
            res = dfs(r + 1, cols, diags, antidiags, n, res)
            cols.remove(c) 
            diags.remove(diag) 
            antidiags.remove(antidiag)
        return res
   
    return dfs(0, set(), set(), set(), n, 0)

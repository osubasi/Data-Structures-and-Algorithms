# Omer Subasi

def gen_parentheses(n):
    res = []
    def backtrack(seq, open, close):
        if not open and not close:
            res.append(seq)
            return
        if open:
            backtrack(seq + "(", open - 1, close)
        if close > open:
            backtrack(seq + ")", open, close - 1)
    
    backtrack("", n, n)
    return res

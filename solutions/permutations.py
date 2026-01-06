# Omer Subasi

def permutation(arr):
    
  def backtrack(curr):
        if len(curr) == len(arr):
            res.append(curr[:])
            return

        for n in arr:
            if n not in curr:
                curr.append(n)
                backtrack(curr)
                curr.pop()

    res = []
    backtrack([])
    return res

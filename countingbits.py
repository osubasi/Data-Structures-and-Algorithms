# Omer Subasi

def countBits(n):
    res = [] 
    for x in range(n + 1):
        s = 0
        while x:
            s += x & 1
            x = x >> 1 
        res.append(s)
    return res

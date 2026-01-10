# Omer Subasi

def hammingDistance(x, y):
    d = 0
    while x or y:
        d += (x & 1) ^ (y & 1)
        x = x >> 1
        y = y >> 1
    
    return d

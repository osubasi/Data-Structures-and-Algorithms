# Omer Subasi

def reverseBits(n):
    i = 0
    r = 0
    while n:
        r += 2**(31-i) * (n & 1)
        i += 1
        n = n >> 1 
    
    return r

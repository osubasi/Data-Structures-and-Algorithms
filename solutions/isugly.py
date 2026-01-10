# Omer Subasi

def isUgly(n):
    if n < 0:
        return False
    if n == 1:
        return True
    d = n
    while d >= 1 and d % 2 == 0:
        d = d / 2
    while d >= 1 and d % 3 == 0:
        d = d / 3
    while d >= 1 and d % 5 == 0: 
        d = d / 5
    
    return d == 1

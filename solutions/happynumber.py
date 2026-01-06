# Omer Subasi

def isHappy(n):
    seen = set()
    while n not in seen:
        seen.add(n)
        s = [int(c)*int(c) for c in str(n)]
        n = sum(s)
    return n==1

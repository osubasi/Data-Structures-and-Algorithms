# Omer Subasi

import math

def sumofSquareSum(c):
    s_c = math.sqrt(c)
    print(int(s_c))
    memo = set()
    for x in range(int(s_c)+1):
        if c - x*x in memo:
            return True
        else:
            memo.add(x*x)
            if c - x*x in memo:
                return True

    return False

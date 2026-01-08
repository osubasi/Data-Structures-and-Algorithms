# Omer Subasi

def calculate(s):
    stack = []
    curr = 0
    sign = 1
    res = 0
    for c in s:
        if c.isdigit():
            curr = curr * 10 + int(c)
        elif c == "+" or c == "-":
            res += curr * sign
            if c == "-":
                sign = -1
            else:
                sign = 1
            curr = 0
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ")":
            res += sign * curr
            res *= stack.pop()
            res += stack.pop()
            curr = 0
    
    return res + curr * sign

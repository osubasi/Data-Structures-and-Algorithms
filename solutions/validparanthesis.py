# Omer Subasi

def isValid(s):
    mymap = {'(': ')', '{':'}', '[':']'}
    stack = []
    for c in s:
        if c in mymap:
            stack.append(c)            
        else:
            if stack and mymap[stack[-1]] == c:
                stack.pop()
            else:
                return False
    
    return not stack

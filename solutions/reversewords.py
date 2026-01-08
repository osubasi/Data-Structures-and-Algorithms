# Omer Subasi

def reverseWords(s):
    strs = s.split()
    res = ""
    for i in range(len(strs)-1, -1, -1):
        res += strs[i] + " "
    
    return res[:-1]

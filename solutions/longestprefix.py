# Omer Subasi

def longestCommonPrefix(strs):
    lres = float('inf')
    res = ""
    n = len(strs)
    for i in range(n):
        if (len(strs[i]) < lres):
            res = strs[i]
            lres =  len(strs[i])
    
    if not res:
        return ""
    
    for i in range(len(res)):
        for j in range(n):
            if res[i] != strs[j][i]:
                return res[:i]

    return res

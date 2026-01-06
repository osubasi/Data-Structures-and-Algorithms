# Omer Subasi

def strStr(haystack, needle):
    n = len(needle)
    m = len(haystack)
    for i in range(0, m - n + 1):
        if needle == haystack[i:i + n]:
            return i
    return -1

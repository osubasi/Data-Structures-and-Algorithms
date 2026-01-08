# Omer Subasi

def longestSubstringUnique(s):
    n = len(s)
    max_l = 0
    curr = set()
    left = right = 0
    while right < n:
        while s[right] in curr:
            curr.remove(s[left])
            left += 1
          
        max_l = max(max_l, right - left + 1)
        curr.add(s[right])
        right += 1
    
    return max_l

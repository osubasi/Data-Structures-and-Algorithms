# Omer Subasi

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    freq1 = {}
    freq2 = {}
    for i in range(len(s)):
        if s[i] not in freq1:
            freq1[s[i]] = 1
        else:
            freq1[s[i]] += 1
        
        if t[i] not in freq2:
            freq2[t[i]] = 1
        else:
            freq2[t[i]] += 1

    if freq1.keys() != freq2.keys():
        return False
    
    for c in s:
        if freq1[c] != freq2[c]:
            return False
    return True

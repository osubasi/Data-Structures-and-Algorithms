# Omer Subasi

def betterCompression(compressed):
    i = 0
    n = len(compressed)
    freqs = {}
    while i < n:
        if compressed[i].isalpha():
            j = i + 1
            tmp = ""
            while j < n:
                if compressed[j].isdigit():
                    tmp += compressed[j]
                    j += 1
                else:
                    break
            
            if compressed[i] not in freqs:
                freqs[compressed[i]] = int(tmp)
            else:
                freqs[compressed[i]] += int(tmp)
        i += 1
    
    res = ""
    sortedkeys = sorted(freqs.keys())
    for k in sortedkeys:
        res += k + str(freqs[k])
    
    return res

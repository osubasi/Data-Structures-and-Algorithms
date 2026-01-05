# Omer Subasi

def reversePrefix(word, ch):
        res = ''
        idx = -1
        for i in range(len(word)):
            if word[i] == ch:
                pre = word[:i+1]
                j =  i
                idx = i
                while j >= 0:
                    res += pre[j]
                    j -= 1
                break
        
        if idx == -1:
            return word
        else: return res+word[idx+1:]

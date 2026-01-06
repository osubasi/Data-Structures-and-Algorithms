# Omer Subasi

def lengthOfLastWord(s):
    last = ''
    curr = ''
    for c in s:
        if c != ' ':
            curr += c
        else:
            if curr != '':
                last = curr
                curr = ''
    
    if curr != '':
        last = curr

    return len(last)

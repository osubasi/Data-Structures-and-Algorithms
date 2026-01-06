# Omer Subasi

def arraySign(nums):
    p = 1
    for num in nums:
        p *= num
    
    if(p > 0): return 1
    if(p < 0): return -1
    if(p == 0): return 0

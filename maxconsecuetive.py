# Omer Subasi

def findMaxConsecutiveOnes(nums):
    curr = 0
    res = 0
    for i in range(len(nums)):
        if nums[i] == 1:        
            curr += 1
        else:
            res = max(res, curr)
            curr = 0
    
    return max(res, curr)

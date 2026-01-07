# Omer Subasi

def goodPairs(nums):
    n = len(nums)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                cnt += 1
    
    return cnt

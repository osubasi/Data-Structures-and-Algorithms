# Omer Subasi 

def canjump(nums):
    for i in range(len(nums) - 1, 0, -1):
        if not nums[i - 1]:
            return False
        if nums[i - 1] + i < nums[i]:
            return False
    return True

# Omer Subasi

def maxMinPairSum(nums):
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(0, n, 2):
            res += nums[i]
          
        return res

# Omer Subasi

def singleNumber(nums):
        res = 0
        for x in nums:
            res ^= x
        return res

# Omer Subasi

def prefixSum(nums):
    s = 0
    res = []
    for x in nums:
        s += x
        res.append(s)
    return res

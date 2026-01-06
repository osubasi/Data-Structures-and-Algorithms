# Omer Subasi

from collections import Counter

def topKFrequent(nums, k): 
    if k == len(nums):
        return nums
    count = Counter(nums) 
    return heapq.nlargest(k, count.keys(), key=count.get) 

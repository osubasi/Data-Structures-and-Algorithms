# Omer Subasi

def twoSum(nums, target):
        store = {}
        for i, x in enumerate(nums):
            store[x] = i

        for i, x in enumerate(nums):
            if target - x in store and store[target - x] != i:
                return [i, store[target - x]]
            
        return []

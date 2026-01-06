# Omer Subasi

def containsDuplicate(nums):
    myset = set()
    for num in nums:
        if num in myset:
            return True
        else:
            myset.add(num)
    
    return False

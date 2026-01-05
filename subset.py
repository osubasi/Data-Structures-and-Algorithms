def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        def backtrack(i):
            if i == len(nums):
                res.append(curr[:])
                return
            else:
                curr.append(nums[i])
                backtrack(i+1)
                curr.pop()
                backtrack(i+1)
        
        backtrack(0)
        return res

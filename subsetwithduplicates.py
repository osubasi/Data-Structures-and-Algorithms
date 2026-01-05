  def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
      res = set()
      curr = []
      def backtrack(i):
          if i == len(nums):
              res.add(tuple(curr[:]))
              return
          else:
              curr.append(nums[i])
              backtrack(i+1)
              curr.pop()
              backtrack(i+1)
      
      nums.sort()
      backtrack(0)
      return list(res)

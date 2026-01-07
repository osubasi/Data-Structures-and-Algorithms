# Omer Subasi

def flipsfromStarttoGoal(start, goal):
      tmp = start ^ goal
      res = 0
      while tmp:
          res += tmp & 1
          tmp = tmp>>1
        
      return res

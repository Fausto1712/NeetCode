class Solution:
    def maxUniqueSplit(self, s: str) -> int:
         
       def dfs(i, curr_set):
           if i == len(s):
            return 0
           
           res = 0
           for j in range(i, len(s)):
              subtr = s[i:j+1]
              if subtr in curr_set:
                 continue
              curr_set.add(subtr)
              res = max(res, 1+ dfs(j+1, curr_set))
              curr_set.remove(subtr)
            
           return res
       
       return dfs(0, set())


if __name__ == "__main__":
    solution = Solution()
    s = "aba"
    print(f"The solution is: {solution.maxUniqueSplit(s)}")
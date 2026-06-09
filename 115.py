from typing import List

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, curr):
            if i == len(s):
                if curr == t:
                    return 1
                else:
                    return 0
            if t[:len(curr)] != curr:
                return 0
                
            if (i, curr) in dp:
                return dp[(i, curr)]
            
            dp[(i, curr)] = dfs(i+1, curr + s[i]) + dfs(i+1, curr)
            return dp[(i, curr)]

        return dfs(0, "")
        
    
if __name__ == "__main__":
    solution = Solution()

    s = "rabbbit"
    t = "rabbit"
    print(f"Result: {solution.numDistinct(s,t)}")


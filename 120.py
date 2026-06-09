from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[float("infinity")] * len(triangle[r]) for r in range(len(triangle))]
        
        def dfs(i,pos):
            if memo[i][pos] != float("infinity"):
                return memo[i][pos]
            if i == len(triangle)-1:
                memo[i][pos] = triangle[i][pos]
                return triangle[i][pos]
            
            memo[i][pos] = triangle[i][pos] + min(dfs(i+1, pos), dfs(i+1,pos+1))
            return memo[i][pos]
        
        return dfs(0,0)
    
class Solution:
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        dp = [[float("infinity")] * len(triangle[r]) for r in range(len(triangle))]

        for i in range(len(triangle)-1, -1, -1):
            for j in range(len(triangle[i])-1, -1 ,-1):
                if i == len(triangle)-1:
                    dp[i][j] = triangle[i][j]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]


        
    
if __name__ == "__main__":
    solution = Solution()

    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(f"Result: {solution.minimumTotal2(triangle)}")


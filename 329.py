from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        dp = [[0] * m for _ in range(n)]

        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            best = 1

            if i+1 < n and matrix[i][j] < matrix[i+1][j]:
                best = max(best,dfs(i+1,j)+1)
            if i-1 >= 0 and matrix[i][j] < matrix[i-1][j]:
                best = max(best,dfs(i-1,j)+1)
            if j+1 < m and matrix[i][j] < matrix[i][j+1]:
                best = max(best,dfs(i,j+1)+1)
            if j-1 >= 0 and matrix[i][j] < matrix[i][j-1]:
                best = max(best,dfs(i,j-1)+1)
            
            dp[i][j] = best
            return dp[i][j]
        
        res = 0

        for i in range(n):
            for j in range(m):
                if dp[i][j] == 0:
                    dfs(i,j)
                res = max(res, dp[i][j])

        return res

    
if __name__ == "__main__":
    solution = Solution()

    matrix = [[1,2], [2,2], [2,2]]
    print(f"Result: {solution.longestIncreasingPath(matrix)}")


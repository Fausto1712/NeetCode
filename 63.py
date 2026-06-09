from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        dp = [[0] * (m+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(0, n):
            for j in range(0, m):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i == 0:
                    dp[i][j] += dp[i][j-1]
                elif j == 0:
                    dp[i][j] += dp[i-1][j]
                else:
                    dp[i][j] += dp[i-1][j] + dp[i][j-1]

        return dp[n-1][m-1]


if __name__ == "__main__":
    solution = Solution()
    obstacleGrid = [[0,0]]

    print(f"Result: {solution.uniquePathsWithObstacles(obstacleGrid)}")

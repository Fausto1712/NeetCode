from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        dp = [[0] * cols for _ in range(rows)]

        validTiles = []

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    dp[row][col] = 1
                else:
                    if heights[row-1][col] <= heights[row][col]:
                        dp[row][col] = max(dp[row-1][col], dp[row][col])
                    if heights[row][col-1] <= heights[row][col]:
                        dp[row][col] = max(dp[row][col-1], dp[row][col])
        
        for row in range(rows-1, -1, -1):
            for col in range(cols-1,-1, -1):
                if row == rows-1 or col == cols-1:
                    dp[row][col] += 2
                else: 
                    if heights[row+1][col] <= heights[row][col]:
                        if dp[row+1][col] == 3 or (dp[row+1][col] == 2 and dp[row][col] == 1):
                            dp[row][col] = 3
                        elif dp[row+1][col] == 2:
                            dp[row][col] = 2
                    if heights[row][col+1] <= heights[row][col]:
                        if dp[row][col+1] == 3 or (dp[row][col+1] == 2 and dp[row][col] == 1):
                            dp[row][col] = 3
                        elif dp[row+1][col] == 2:
                            dp[row][col] = 2

                if dp[row][col] == 3:
                    validTiles.append([row,col])
        
        return validTiles
        
if __name__ == "__main__":
    solution = Solution()

    heights = [[10,10,10],[10,1,10],[10,10,10]]
    print(f"Result: {solution.pacificAtlantic(heights)}")
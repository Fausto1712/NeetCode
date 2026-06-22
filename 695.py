from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maxIsland = 0

        def mapIsland(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0
            return 1 + mapIsland(row-1, col) + mapIsland(row+1, col) + mapIsland(row, col-1) + mapIsland(row, col+1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    maxIsland = max(maxIsland, mapIsland(row, col))
    
        return maxIsland
                
if __name__ == "__main__":
    solution = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(f"Solution {solution.maxAreaOfIsland(grid)}")
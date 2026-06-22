from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0] * cols for _ in range(rows)]
        islands = 0

        def mapIsland(row, col):
            nonlocal visited
            if row >= rows or col >= cols or row < 0 or col < 0 or row >= rows or col >= cols or row < 0 or col < 0 or grid[row][col] == "0" or visited[row][col]:
                return 0
            
            visited[row][col] = 1

            mapIsland(row-1, col)
            mapIsland(row+1, col)
            mapIsland(row, col-1)
            mapIsland(row, col+1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and not visited[row][col]:
                    islands += 1
                    mapIsland(row, col)
    
        return islands
                
if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Solution {solution.numIslands(grid)}")
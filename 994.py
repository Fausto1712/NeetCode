from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        minMinutes = 0
        q = deque()

        def isValid(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

        while q:
            r, c, minutes = q.popleft()
            minMinutes = max(minMinutes, minutes)

            if isValid(r - 1, c) and grid[r - 1][c] == 1:
                grid[r - 1][c] = 2
                q.append((r - 1, c, minutes + 1))

            if isValid(r + 1, c) and grid[r + 1][c] == 1:
                grid[r + 1][c] = 2
                q.append((r + 1, c, minutes + 1))

            if isValid(r, c - 1) and grid[r][c - 1] == 1:
                grid[r][c - 1] = 2
                q.append((r, c - 1, minutes + 1))

            if isValid(r, c + 1) and grid[r][c + 1] == 1:
                grid[r][c + 1] = 2
                q.append((r, c + 1, minutes + 1))

        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return minMinutes


if __name__ == "__main__":
    solution = Solution()
    n = 5
    grid = [[2,1,1],[0,1,1],[1,0,1]]

    print(solution.orangesRotting(grid))
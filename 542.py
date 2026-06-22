from typing import List
from collections import deque
from math import inf

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        queue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = float('inf')
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[r][c] + 1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
        
        return mat
    
    def updateMatrix2(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    continue
                mat[r][c] = min(
                    inf if c == 0 else mat[r][c-1],
                    inf if r == 0 else mat[r-1][c]
                ) + 1
        
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if mat[r][c] == 0:
                    continue
                mat[r][c] = min(
                    mat[r][c],
                    inf if c == n-1 else mat[r][c+1] + 1,
                    inf if r == m-1 else mat[r+1][c] + 1
                )
        
        return mat
        
if __name__ == "__main__":
    solution = Solution()

    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(f"Result: {solution.updateMatrix(mat.copy())}")
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    print(f"Result: {solution.updateMatrix2(mat.copy())}")
from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = [[0]* cols for _ in range(rows)]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(row, col):
            queue = deque()
            queue.append([row,col])
            visited[row][col] = 1

            while queue:
                r, c = queue.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and board[nr][nc] == "O":
                        queue.append([nr, nc])
                        visited[nr][nc] = 1

        for row in range(rows):
            if board[row][0] == "O":
                bfs(row,0)

            if board[row][cols-1] == "O":
                bfs(row,cols-1)

        
        for col in range(cols):
            if board[0][col] == "O":
                bfs(0, col)
            if board[rows-1][col] == "O":
                bfs(rows-1, col)

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and not visited[row][col]:
                    board[row][col] = "X"
        
if __name__ == "__main__":
    solution = Solution()

    board = [["O","O","O"],["O","O","O"],["O","O","O"]]
    solution.solve(board)
    print("Result:", board)
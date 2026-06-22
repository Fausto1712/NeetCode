from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])

        visited = {}
        provinces = 0

        def dfs(row):
            visited[row] = 1
            for col in range(cols):
                if isConnected[row][col] == 1 and col not in visited:
                    dfs(col)

        for row in range(rows):
            if row not in visited:
                provinces += 1
                dfs(row)

        return provinces

        
if __name__ == "__main__":
    solution = Solution()

    isConnected = [[1,1,0],[1,1,0],[0,0,1]]
    print("Result:", solution.findCircleNum(isConnected))
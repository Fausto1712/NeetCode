from typing import List

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        dp = {}

        def dfs(row: int, col: int, maxMove:int):
            if (row,col,maxMove) in dp:
                return dp[(row,col,maxMove)]
            if maxMove == 0:
                return 0
            currSum = 0

            if (row+1) >= m:
                currSum += 1
            else:
                currSum += dfs(row+1,col,maxMove-1)

            if row-1 < 0:
                currSum += 1
            else:
                currSum += dfs(row-1,col,maxMove-1)

            if (col+1) >= n:
                currSum += 1
            else:
                currSum += dfs(row,col+1,maxMove-1)

            if col-1 < 0:
                currSum += 1
            else:
                currSum += dfs(row,col-1,maxMove-1)

            dp[(row,col,maxMove)] = currSum % mod
            return dp[(row,col,maxMove)]
            
        return dfs(startRow, startColumn, maxMove)
    
if __name__ == "__main__":
    solution = Solution()

    m = 2
    n = 2
    maxMove = 2
    startRow = 0
    startColumn = 0
    print(f"Result: {solution.findPaths(m,n,maxMove,startRow, startColumn)}")


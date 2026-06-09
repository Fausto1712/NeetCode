from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        count = 0

        for i in range(n):
            if matrix[i][0] != 0:
                count += 1
        
        for j in range(1,m):
            if matrix[0][j] != 0:
                count += 1

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]) + 1
                    count += matrix[i][j]

        return count


if __name__ == "__main__":
    solution = Solution()

    matrix = [[1,0,1],[1,1,0],[1,1,0]]
    
    print(f"Result: {solution.countSquares(matrix)}")


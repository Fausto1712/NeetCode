from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1,n):
            for j in range(m):
                matrix[i][j] += min(matrix[i-1][c] for c in range(max(0, j-1), min(m, j+2)))

        return min(matrix[-1])
        
    
if __name__ == "__main__":
    solution = Solution()

    matrix = [[2,1,3],[6,5,4],[7,8,9]]
    print(f"Result: {solution.minFallingPathSum(matrix)}")


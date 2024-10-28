from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = (len(matrix) * len(matrix[0]))-1
        while left <= right:
            m = left + ((right - left) // 2)
            if target > matrix[m // len(matrix[0])][m % len(matrix[0])]:
                left = m + 1
            elif target < matrix[m // len(matrix[0])][m % len(matrix[0])]:
                right = m - 1
            else:
                return True
        return False

matrix = [[1]]

print()
print(f"Is in matrix: {Solution.searchMatrix(Solution, matrix, 2)}")
print()
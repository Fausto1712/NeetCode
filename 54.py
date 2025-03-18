from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        right = len(matrix[0])
        left = 0
        bottom = len(matrix)
        top = 0
        while True:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            if len(res) == (len(matrix) * len(matrix[0])):
                return res
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1
            if len(res) == (len(matrix) * len(matrix[0])):
                return res
            for i in range(right, left, -1):
                res.append(matrix[bottom-1][i-1])
            bottom -= 1
            if len(res) == (len(matrix) * len(matrix[0])):
                return res
            for i in range(bottom, top, -1):
                res.append(matrix[i-1][left])
            left += 1
            if len(res) == (len(matrix) * len(matrix[0])):
                return res


print()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(f"Spiral Order is: {Solution.spiralOrder(Solution, matrix)}")
print()
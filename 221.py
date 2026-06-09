from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])

        best = 0

        for i in range(n):
            best = max(best, int(matrix[i][0]))
        for j in range(m):
            best = max(best, int(matrix[0][j]))

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != "0":
                    matrix[i][j] = min(int(matrix[i-1][j-1]), int(matrix[i-1][j]) , int(matrix[i][j-1])) + 1
                    best = max(best, matrix[i][j])

        return best * best

    def maximalSquareOpt(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [0] * (m + 1)
        best = 0

        for i in range(1, n + 1):
            prev = 0
            for j in range(1, m + 1):
                temp = dp[j]
                if matrix[i - 1][j - 1] == "1":
                    dp[j] = min(dp[j], dp[j - 1], prev) + 1
                    best = max(best, dp[j])
                else:
                    dp[j] = 0
                prev = temp

        return best * best
    
if __name__ == "__main__":
    solution = Solution()

    matrix = [["0","1"],["1","0"]]
    print(f"Result: {solution.maximalSquare(matrix)}")
    print(f"Result Opt: {solution.maximalSquareOpt(matrix)}")


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        for i in range(n):
            solutions.append("")
            for j in range(n):
                solutions[i] += "."
                
        return solutions
        


if __name__ == "__main__":
    solution = Solution()
    n = 4
    print(f"The possible arrangements are: {solution.solveNQueens(n)}")
        
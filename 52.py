from typing import List

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        col = [0] * n
        diag1 = [0] * (n*2 -1)
        diag2 = [0] * (n*2 -1)
        def search(k):
            if n == k:
                solutions.append([])
                return
            
            for i in range(n):
                if (col[i] or diag1[i+k] or diag2[i-k+n-1]): continue
                col[i], diag1[i+k], diag2[i-k+n-1] = 1,1,1
                search(k+1)
                col[i], diag1[i+k], diag2[i-k+n-1] = 0,0,0
        
        search(0)
        return len(solutions)
        


if __name__ == "__main__":
    solution = Solution()
    n = 5
    print(f"The possible arrangements are: {solution.totalNQueens(n)}")
        
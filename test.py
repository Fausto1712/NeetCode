from typing import List

class Solution:
    def testingProblem(self, n) -> int:
        res = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                res.append(i)
                if i != n // i:
                    res.append(n // i)
            i += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    n = 1600
    print(f"The solution is {solution.testingProblem(n)}")
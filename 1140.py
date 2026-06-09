from typing import List
from functools import cache
from itertools import accumulate

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}

        def dfs(taking, M, rPiles):
            if not rPiles:
                return 0
            key = (taking, M, tuple(rPiles))
            if key in dp:
                return dp[key]
            
            best = 0 if taking else float("infinity")
            for i in range(1, min(2 * M, len(rPiles)) + 1):
                if taking:
                    best = max(best, sum(rPiles[:i]) + dfs(False, max(M, i), rPiles[i:]))
                else:
                    best = min(best, dfs(True, max(M, i), rPiles[i:]))
            
            dp[key] = best
            return dp[key]

        return dfs(True, 1, piles)
    
    def stoneGameIIOpt(self, piles: List[int]) -> int:
        n = len(piles)
        s = sum(piles)
        suf = list(accumulate(piles[::-1]))[::-1]

        @cache
        def dfs(i: int, M: int) -> int:
            if i == n:
                return 0
            if 2 * M >= n - i:
                return suf[i]
            ans = s
            for x in range(1, 2 * M + 1):
                ans = min(ans, dfs(i + x, max(x, M)))
            return suf[i] - ans

        return dfs(0, 1)
    
if __name__ == "__main__":
    solution = Solution()

    piles = [2,7,9,4,4]
    print(f"Result: {solution.stoneGameII(piles)}")
    print(f"Result: {solution.stoneGameIIOpt(piles)}")


from typing import List

class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = {}

        def dfs(i, last):
            if i == len(s):
                return 0

            if (i, last) in dp:
                return dp[(i, last)]

            res = dfs(i+1, last)

            if last is None or abs(ord(last) - ord(s[i])) <= k:
                res = max(res, dfs(i+1, s[i]) + 1)

            dp[(i, last)] = res
            return res

        return dfs(0, None)

    def longestIdealStringDP(self, s: str, k: int) -> int:
        dp = [0] * 26

        for ch in s:
            i = ord(ch) - ord('a')
            best = 0
            for c in range(max(0, i-k), min(26, i+k+1)):
                best = max(best, dp[c])
            dp[i] = best + 1

        return max(dp)

    
if __name__ == "__main__":
    solution = Solution()

    s = "eduktdb"
    k = 2
    print(f"Result: {solution.longestIdealString(s,k)}")
    print(f"Result DP: {solution.longestIdealStringDP(s,k)}")


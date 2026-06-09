from typing import List

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}

        def dfs(i,curr):
            if i == n:
                if curr == target:
                    return 1
                else:
                    return 0
                
            if (i,curr) in dp:
                return dp[(i,curr)]
            
            sum = 0
            for x in range(1,k+1):
                sum += dfs(i+1,curr+x)

            dp[(i,curr)] = sum
            return dp[(i,curr)]

        return dfs(0,0) % (10**9 + 7)

    def numRollsToTargetDP(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (target + 1)
        dp[0] = 1

        for _ in range(n):
            prefix = [0] * (target + 2)
            for j in range(target + 1):
                prefix[j + 1] = (prefix[j] + dp[j]) % MOD

            ndp = [0] * (target + 1)
            for j in range(1, target + 1):
                lo = max(0, j - k)
                ndp[j] = (prefix[j] - prefix[lo]) % MOD

            dp = ndp

        return dp[target]

    
if __name__ == "__main__":
    solution = Solution()

    n, k, target = 1, 6, 3
    print(f"Result: {solution.numRollsToTarget(n, k, target)}")
    print(f"Result DP: {solution.numRollsToTargetDP(n, k, target)}")

    n, k, target = 2, 6, 7
    print(f"Result: {solution.numRollsToTarget(n, k, target)}")
    print(f"Result DP: {solution.numRollsToTargetDP(n, k, target)}")

    n, k, target = 30, 30, 500
    print(f"Result: {solution.numRollsToTarget(n, k, target)}")
    print(f"Result DP: {solution.numRollsToTargetDP(n, k, target)}")


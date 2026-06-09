class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        dp = {}

        def dfs(amount):
            if amount == 1:
                return 0
            if amount in dp:
                return dp[amount]

            best = amount
            i = 2
            while i*i <= amount:
                if amount%i == 0:
                    best = min(best, dfs(i)+amount//i)
                    best = min(best, dfs(amount//i)+i)
                i += 1

            dp[amount] = best
            return best

        return dfs(n)
    
if __name__ == "__main__":
    solution = Solution()

    n = 3
    print(f"Result: {solution.minSteps(n)}")


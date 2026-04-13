from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] += dp[i - c]

        return dp[amount]
    
if __name__ == "__main__":
    solution = Solution()

    coins = [1,2,5]
    amount = 5
    print(f"Result: {solution.change(amount,coins)}")


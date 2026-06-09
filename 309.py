from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (n+1) for _ in range(n+1)]
        
        for i in range(1, n):
            for j in range(i, n):
                dp[i][j] = max(dp[i][j-1], dp[i-1][j], prices[j] - prices[i-1])
                if i >= 4 and i == j:
                    prevBest = dp[i-3][j-3]
                if i >= 4:
                    dp[i][j] = max(dp[i][j], prices[j] - prices[i-1] + prevBest)

        return dp[n-1][n-1]
    
    def maxProfitOP(self, prices: List[int]) -> int:
        n = len(prices)
        next_buy, next_sell = 0, 0
        after_cooldown_buy = 0

        for i in range(n - 1, -1, -1):
            curr_buy = max(next_sell - prices[i], next_buy)
            curr_sell = max(after_cooldown_buy + prices[i], next_sell)
            after_cooldown_buy = next_buy
            next_buy, next_sell = curr_buy, curr_sell

        return next_buy
    
    def maxProfitDFS(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i,buying)]
            
            hold = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, False) - prices[i]
                dp[(i,buying)] = max(hold, buy)
            else:
                sell = dfs(i+2, True) + prices[i]
                dp[(i,buying)] = max(sell, hold)
            return dp[(i,buying)]
        
        return dfs(0, True)
        
        

if __name__ == "__main__":
    solution = Solution()
    prices = [1,2,3,0,2,5]

    print(f"Result: {solution.maxProfit(prices)}")
    print(f"Result: {solution.maxProfitOP(prices)}")

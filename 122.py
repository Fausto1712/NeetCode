from typing import List

class Solution:
    def maxProfitLogic(self, prices: List[int]) -> int:
        res = 0
        previous = prices[0]
        for i in range(1, len(prices)):
            cur = prices[i]
            if cur > previous:
                res += cur - previous
            previous = cur
        return res

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            hold = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, False) - prices[i]
                dp[(i, buying)] = max(buy, hold)
            else:
                sell = dfs(i+1, True) + prices[i]
                dp[(i, buying)] = max(sell, hold)
            return dp[(i, buying)]
            
        return dfs(0, True)

if __name__ == "__main__":
    solution = Solution()
    prices = [7,1,5,3,6,4]

    print(f"Result: {solution.maxProfit(prices)}")
    print(f"Result: {solution.maxProfitLogic(prices)}")

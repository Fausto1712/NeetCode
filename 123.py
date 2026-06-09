from typing import List

class Solution:
    def maxProfitSense(self, prices: List[int]) -> int:
        if not prices:
            return 0
            
        buy1, buy2 = float('inf'), float('inf')
        profit1, profit2 = 0, 0
        
        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            
        return profit2

    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying, totalTrans):
            if len(prices) <= i:
                return 0
            if (i, buying, totalTrans) in dp:
                return dp[(i, buying, totalTrans)]
            
            hold = dfs(i+1, buying, totalTrans)

            if buying and totalTrans < 2:
                buy = dfs(i+1, False, totalTrans) - prices[i]
                dp[(i, buying, totalTrans)] = max(buy, hold)
            elif totalTrans < 2:
                sell = dfs(i+1, True, totalTrans+1) + prices[i]
                dp[(i, buying, totalTrans)] = max(sell, hold)
            else:
                return dfs(i+1, buying, totalTrans)
            return dp[(i, buying, totalTrans)]

        return dfs(0, True, 0)
        

if __name__ == "__main__":
    solution = Solution()
    prices = [3,3,5,0,0,3,1,4]

    print(f"Result: {solution.maxProfit(prices)}")
    print(f"Result: {solution.maxProfitSense(prices)}")
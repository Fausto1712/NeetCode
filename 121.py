from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        profit = 0
        for p in prices[1:]:
            if minBuy > p:
                minBuy = p
            profit = max(profit,p - minBuy)

        return profit
        

prices = [7,1,5,3,6,4]

print()
print(f"Max profit: {Solution.maxProfit(Solution, prices)}")
print()
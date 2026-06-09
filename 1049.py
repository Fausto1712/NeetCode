from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        dp = [0] * (target + 1)

        for stone in stones:
            for t in range(target, stone - 1, -1):
                dp[t] = max(dp[t], dp[t - stone] + stone)

        return stoneSum - 2 * dp[target]
            
        
        

if __name__ == "__main__":
    solution = Solution()
    stones = [2,7,4,1,8,1]

    print(f"Result: {solution.lastStoneWeightII(stones)}")

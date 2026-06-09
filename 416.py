from typing import List

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False
        mid = (sum(nums) // 2)
        dp = [False] * (mid + 1)
        dp[0] = True

        for num in nums:
            for j in range(1, mid):
                if (num - j) > 0:
                    dp[j] = dp[num - j]
        
        return dp[-1]
    
if __name__ == "__main__":
    solution = Solution()

    nums = [11,5,11,5]
    print(f"Result: {solution.canPartition(nums)}")


from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n-2, -1, -1):
            if nums[i] > 0:
                dp[i] = 1 + min(dp[i + 1 : i + nums[i] + 1])
            else:
                dp[i] = float("infinity")

        return dp[0]

nums = [2,3,1,1,4]

print()
print(f"Solution: {Solution.jump(Solution, nums)}")
print()
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSolution = nums[0]
        curr = 0
        for i in range(len(nums)):
            if curr < 0:
                curr = nums[i]
            else:
                curr += nums[i]
            maxSolution = max(maxSolution, curr)

        return maxSolution
    
    def maxSubArrayDP(self, nums: List[int]) -> int:
        dp = [*nums]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)


        

if __name__ == "__main__":
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(f"The solution is {solution.maxSubArray(nums)}")
    print(f"The solution is {solution.maxSubArrayDP(nums)}")
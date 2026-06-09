from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def dfs(i, curr):
            if i == n:
                if curr == target:
                    return 1
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            
            dp[(i, curr)] = dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
            return dp[(i, curr)]

        return dfs(0,0)

    def findTargetSumWaysDP(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # {current_sum: number_of_ways}

        for num in nums:
            next_dp = {}
            for curr, ways in dp.items():
                next_dp[curr + num] = next_dp.get(curr + num, 0) + ways
                next_dp[curr - num] = next_dp.get(curr - num, 0) + ways
            dp = next_dp

        return dp.get(target, 0)

    
if __name__ == "__main__":
    solution = Solution()

    nums = [30,1,5,32,16,17,30,29,48,14,29,4,31,12,40,13,13,20,41,38]
    target = 9
    print(f"Result: {solution.findTargetSumWays(nums,target)}")


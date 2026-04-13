from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n

        def dfs(i):
            if memo[i] != -1:
                return memo[i]
            
            maxCount = nums[i]
            for j in range(i+2,n):
                maxCount = max(maxCount,nums[i] + dfs(j))

            memo[i] = maxCount
            return maxCount
        
        return max(dfs(i) for i in range(n))
        


if __name__ == "__main__":
    solution = Solution()

    nums = [2,7,9,3,1]
    print(f"Result: {solution.rob(nums)}")
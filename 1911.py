from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}

        def dfs(i,adding):
            if i == n:
                return 0
            if (i, adding) in dp:
                return dp[(i,adding)]
            
            best = dfs(i+1, adding)

            if adding:
                curr =  dfs(i+1, False) + nums[i]
            else:
                curr = dfs(i+1, True) - nums[i]

            dp[(i,adding)] = max(best, curr)
            return dp[(i,adding)]

        return dfs(0, True)
    
if __name__ == "__main__":
    solution = Solution()

    nums = [4,2,5,3]
    print(f"Result: {solution.maxAlternatingSum(nums)}")


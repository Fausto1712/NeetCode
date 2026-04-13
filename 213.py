from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0],nums[1])
        
        def robbing(nums):
            n = len(nums)
            memo = [0] * (n)

            memo[0] = nums[0]
            memo[1] = max(nums[0], nums[1])

            for i in range(2, n):
                memo[i] = max(memo[i-1], memo[i-2] + nums[i])
            
            return memo[n-1]
        
        return max(robbing(nums[1:]),robbing(nums[:-1]))
            

if __name__ == "__main__":
    solution = Solution()

    nums = [1,2,3,1]
    print(f"Result: {solution.rob(nums)}")


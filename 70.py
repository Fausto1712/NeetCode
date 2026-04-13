from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * n
        memo[0] = 1
        memo[1] = 2

        for i in range(2,n):
            memo[i] = max(memo[i-1]+1, memo[i-2]+2)    

        return memo[-1]        

if __name__ == "__main__":
    solution = Solution()

    nums = 2
    print(f"Result: {solution.climbStairs(nums)}")


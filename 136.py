from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,1,2,4]
    print(f"The single number is: {solution.singleNumber(nums)}")
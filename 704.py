from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            m = left + ((right - left) // 2)
            if target > nums[m]:
                left = m + 1
            elif target < nums[m]:
                right = m - 1
            else:
                return m
        return -1

nums = [-1,0,3,5,9,12]

print()
print(f"Position: {Solution.search(Solution, nums, 2)}")
print()
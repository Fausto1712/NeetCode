from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        
        if nums[l] < nums[r]:
            return nums[l]
        
        while r - l > 1:
            m = l + (r - l) // 2
            if nums[l] < nums[m]:
                l = m
            else:
                r = m
        return min(nums[l], nums[r])

nums = [4,5,6,7,0,1,2]

print()
print(f"Result: {Solution.findMin(Solution, nums)}")
print()
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                currSum = nums[l] + nums[r] + nums[i]
                if currSum < 0:
                    l += 1
                elif currSum > 0:
                    r -= 1
                else:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res
            
    
nums = [0,0,0,0]

print()
print(f"Solution: {Solution.threeSum(Solution,nums)}")
print()
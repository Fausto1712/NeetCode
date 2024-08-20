from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        nums2 = set(nums)
        for k in range(0, len(nums2)-1):
            i = 0
            j = len(nums)-1
            sum = nums[i] + nums[j] + nums[k]
            while (sum != 0) and (i < j):
                if i == k or sum < 0:
                    i+=1
                elif i == j or sum > 0:
                    j-=1
                sum = nums[i] + nums[j] + nums[k]
            if (sum == 0) and (i != k) and (j != k) and (i != j) and (nums[k] != nums[k+1]):
                result.append([nums[i], nums[j],nums[k]]) 
        return result
    
nums = [-4,-1,-1,0,1,2]

print()
print(f"Solution: {Solution.threeSum(Solution,nums)}")
print()
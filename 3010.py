from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        s1 = 1
        s2 = 2
        for i in range(2,len(nums)):
            if nums[s2] >= nums[i] or nums[s1] >= nums[i]:
                if nums[s1] > nums[s2] and i != s2:
                    s1 = s2
                s2 = i
                
        return (nums[0] + nums[s1] + nums[s2])
    
    def minimumCost1line(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])


        


if __name__ == "__main__":
    solution = Solution()
    nums = [1,6,1,5]
    print(f"Best array split cost is: {solution.minimumCost(nums)}")
    print(f"Best array split (1 line) cost is: {solution.minimumCost1line(nums)}")
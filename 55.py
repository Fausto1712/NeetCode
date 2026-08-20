from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                nums[i] = True
            else:
                reachable = False
                for j in range(1, nums[i] + 1):
                    if i + j < len(nums) and nums[i + j] is True:
                        reachable = True
                        break
                nums[i] = True if reachable else False

        return True if nums[0] is True else False
    
    def canJumpOptimal(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

nums = [2,3,1,1,4]

print()
print(f"Solution: {Solution.canJump(Solution, nums)}")
print(f"Solution: {Solution.canJumpOptimal(Solution, nums)}")
print()
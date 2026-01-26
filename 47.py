from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index):
            if index == len(nums):
                res.append(nums.copy())
                return None
            
            for i in range (index, len(nums)):
                if i > index and nums[i] == nums[index]:
                    continue
                nums[index], nums[i] = nums[i], nums[index]
                dfs(index+1)
            
            for i in range(len(nums)-1, index, -1):
                nums[index], nums[i] = nums[i], nums[index]
            
        dfs(0)
        return res
        


if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,3]
    print(f"The solution is: {solution.permuteUnique(nums)}")
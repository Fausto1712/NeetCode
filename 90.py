from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index,subset):
            if index >= len(nums):
                res.append(subset.copy())
                return
            dfs(index+1,subset.copy())
            while index+1 < len(nums) and nums[index] == nums[index+1]:
                subset.append(nums[index])
                index+=1
            subset.append(nums[index])
            dfs(index+1, subset.copy())

        dfs(0,[])
        return res


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,2]
    print(f"The solution is: {solution.subsetsWithDup(nums)}")
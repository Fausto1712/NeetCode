from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(index, perm):
            if index == len(nums):
                res.append(perm.copy())
                return
            
            for i in range(index, len(nums)):
                perm[i], perm[index] = perm[index], perm[i]
                dfs(index+1, perm)
                perm[i], perm[index] = perm[index], perm[i]
        
        dfs(0,nums)
        return res
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3]
    print(f"The solution is: {solution.permute(nums)}")

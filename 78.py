from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(subSet,index):
            if index == len(nums):
                res.append(subSet.copy())
                return None

            dfs(subSet.copy(), index + 1)
            subSet.append(nums[index])
            dfs(subSet.copy(), index +1)
            
        dfs([],0)

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.subsets([1,2,3]))
        
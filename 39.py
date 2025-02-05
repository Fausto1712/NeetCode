from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, combination, sum):
            if index >= len(candidates) or sum > target:
                return
            if sum == target:
                res.append(combination.copy())
                return

            dfs(index+1, combination.copy(),sum)
            sum += candidates[index]
            combination.append(candidates[index])
            dfs(index, combination.copy(),sum)
        
        dfs(0,[],0)
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.combinationSum([2,3,6,7], 7))
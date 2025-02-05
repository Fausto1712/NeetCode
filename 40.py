from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index, combination, sum):
            if sum == target:
                res.append(combination.copy())
                return
            if index == len(candidates) or sum > target:
                return
            
            combination.append(candidates[index])
            dfs(index+1,combination.copy(), sum + candidates[index])
            combination.pop()

            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index+=1 

            dfs(index+1,combination.copy(), sum)
        dfs(0,[],0)
        return res
    
if __name__ == "__main__":
    solution = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(f"Result: {solution.combinationSum2(candidates, target)}")
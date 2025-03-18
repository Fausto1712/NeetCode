from typing import List

class Solution:
    def testingProblem(self, nums: List[int]) -> int:
        total_sum = 0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                min_value = min(nums[i:j+1])
                total_sum += min_value
        
        return total_sum

if __name__ == "__main__":
    solution = Solution()
    array = [3,1,2,4]
    print(f"The solution is {solution.testingProblem(array)}")
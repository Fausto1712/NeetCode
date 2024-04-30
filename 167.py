from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers)-1
        while i < j:
            if (numbers[i] + numbers [j]) < target:
                i += 1
            elif (numbers[i] + numbers [j]) > target:
                j -= 1
            else:
                return [i+1,j+1]
            
numbers = [3,24,50,79,88,150,345]
target = 200

print()
print(f"Solution by brute force: {Solution.twoSum(Solution, numbers, target)}")
print()
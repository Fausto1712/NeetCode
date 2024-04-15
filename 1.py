from typing import List

class Solution:
    """
    Solution with BruteForce, iterate through each one of the elements for every element on the list to check if the pair adds up
    Time complexity: O(n^2)
    """
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return[]

    """
    Solution with HashSet, create the hashTable with every number on the nums List, then iterate a second time through the array
    subtract the current element and check if the result exists on the hashMap, if it does return the direction of the number and the
    hashed Number, if not continue
    Time complexity: O(n)
    """            
    def twoSumHashTableTwo(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            numMap [nums[i]] = i

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap and numMap[complement] != i:
                return [i, numMap[complement]]
        return[]
    
    """
    Optimization with HashSet, iterate through the array subtracting the current element and check if the result exists on the hashMap, if it does return the direction of the number and the
    hashed Number, if not Hash the current number and continue
    Time complexity: O(n)
    """   
    def twoSumHashTableOne(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap [nums[i]] = i
        return[]

nums = [2,7,11,15]
target = 9

print()
print(f"Solution by brute force: {Solution.twoSumBruteForce(Solution,nums,target)}")
print(f"Solution by Hash Two: {Solution.twoSumHashTableTwo(Solution,nums,target)}")
print(f"Solution by Hash One: {Solution.twoSumHashTableOne(Solution,nums,target)}")
print()
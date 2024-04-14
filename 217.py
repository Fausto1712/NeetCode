from typing import List

class Solution:
    """
    Solution with HashSet, check if item is already on hashset, if not store it, if yes return True
    Time complexity: O(n)
    """
    def containsDuplicate(nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
    """
    Solution with BruteForce, for every item check the rest of the array for coincidences
    Time complexity: O(n^2)
    """
    def containsDuplicateBruteForce(nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

    """
    Solution with Sort, sort the array, compare each number with the next and if its equal return True
    Time complexity: O(n)
    """
    def containsDuplicateSort(nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False

nums = [1, 2, 3, 4, 5, 1]
print()
print(f"Solution by hashMap: {Solution.containsDuplicate(nums)}")
print(f"Solution by BruteForce: {Solution.containsDuplicateBruteForce(nums)}")
print(f"Solution by Sorting: {Solution.containsDuplicateSort(nums)}")
print()
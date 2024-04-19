from typing import List

class Solution:
    def longestConsecutiveHash(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if (n-1) not in num_set:
                length = 1
                while (n+length) in num_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortedNums = sorted(nums)
        maxCounter = 1
        counter = 1
        prevNum = sortedNums[0]
        for num in sortedNums:
            if prevNum+1 == num:
                counter += 1
            elif prevNum == num:
                counter = counter
            else:
                counter = 1
            maxCounter = max(maxCounter,counter)
            prevNum = num
        return maxCounter

nums = [9,1,4,7,3,-1,0,5,8,-1,6]

print()
print(f"Solution by sorting: {Solution.longestConsecutiveSorting(Solution, nums)}")
print(f"Solution by Hash: {Solution.longestConsecutiveHash(Solution, nums)}")
print()
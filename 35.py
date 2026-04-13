from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        a,b = 0,len(nums)-1
        while a < b:
            mid = (a+b)//2
            if nums[mid] < target:
                a = mid + 1
            else:
                b = mid
        mid = (a+b)//2
        if nums[mid] < target:
            return mid + 1
        else:
            return mid


if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,5,6]
    target = 7
    print(f"The solution is are: {solution.searchInsert(nums, target)}")
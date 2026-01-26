from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        res = float("infinity")
        nums.sort()
        for i in range(0, len(nums)-k+1):
            res = min(res, nums[i+k-1] - nums[i])
        return res
        


if __name__ == "__main__":
    solution = Solution()
    nums = [90,1,4,5,2]
    k = 2
    print(f"The solution is: {solution.minimumDifference(nums,k)}")
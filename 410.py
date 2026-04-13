from typing import List

class Solution:
    def splitArrayBruteForce(self, nums: List[int], k: int) -> int:
        inf = float("infinity")
        ninf = float("-infinity")
        if len(nums) == k:
            return max(nums)
        elif k == 1:
            return sum(nums)
        
        def dfs(index, current, prev, maxSum):
            if current > k or index > len(nums):
                return inf
            elif current == k:
                return max(maxSum, sum(nums[index-1:]))
            
            return min(dfs(index +1,current,prev,ninf),dfs(index +1,current+1,index+1,max(maxSum,sum(nums[prev:index+1]))))
        
        return dfs(0, 0, 0, inf)
    
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        while True:
            m = (left + right) // 2
            if left >= right:
                return m
            
            current = 0
            counter = 1
            for num in nums:
                current += num
                if current > m:
                    counter += 1
                    current = num
            if counter <= k:
                right = m
            else:
                left = m + 1


if __name__ == "__main__":
    solution = Solution()

    nums = [10,5,13,4,8,4,5,11,14,9,16,10,20,8]
    k = 8
    print(f"Result: {solution.splitArray(nums, k)}")


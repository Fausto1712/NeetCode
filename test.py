from typing import List

class Solution:
    def splitArrayMinimizeMaxSum(self, nums: List[int], k: int) -> int:
        if k > len(nums) or k <= 0:
            return -1
        
        min_largest_sum = float('inf')
        n = len(nums)
        
        def backtrack(start_idx: int, parts_remaining: int, current_max_sum: int):
            nonlocal min_largest_sum
            
            if current_max_sum >= min_largest_sum:
                return
            
            if parts_remaining == 0:
                if start_idx == n:
                    min_largest_sum = min(min_largest_sum, current_max_sum)
                return
            
            if parts_remaining > (n - start_idx):
                return
            
            max_length = n - start_idx - parts_remaining + 1
            
            for length in range(1, max_length + 1):
                current_sum = sum(nums[start_idx:start_idx + length])
                new_max_sum = max(current_max_sum, current_sum)
                
                backtrack(start_idx + length, parts_remaining - 1, new_max_sum)
        
        backtrack(0, k, 0)
        return min_largest_sum if min_largest_sum != float('inf') else -1
    
    def splitArrayShowAllWays(self, nums: List[int], k: int) -> List[tuple]:
        if k > len(nums) or k <= 0:
            return []
        
        result = []
        n = len(nums)
        
        def backtrack(start_idx: int, parts_remaining: int, current_partition: List[List[int]]):
            if parts_remaining == 0:
                if start_idx == n:
                    sums = [sum(part) for part in current_partition]
                    largest_sum = max(sums)
                    result.append((current_partition[:], largest_sum))
                return
            
            if parts_remaining > (n - start_idx):
                return

            max_length = n - start_idx - parts_remaining + 1
            
            for length in range(1, max_length + 1):
                current_part = nums[start_idx:start_idx + length]
                current_partition.append(current_part)
                
                backtrack(start_idx + length, parts_remaining - 1, current_partition)
                
                current_partition.pop()
        
        backtrack(0, k, [])
        return result

if __name__ == "__main__":
    solution = Solution()
    
    nums_large = [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]
    k_large = 8
    
    result_large = solution.splitArrayMinimizeMaxSum(nums_large, k_large)
    print(f"Minimized largest sum: {result_large}")
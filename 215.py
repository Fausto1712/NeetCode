from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)

        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)

        return heap[0]


        
if __name__ == "__main__":
    solution = Solution()

    nums = [3,2,1,5,6,4]
    k = 2
    print("Result:", solution.findKthLargest(nums, k))
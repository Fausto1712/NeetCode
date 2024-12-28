from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        queue = deque()
        maxSlidingWindow = []
        for i in range(len(nums)):
            while queue and nums[i] > queue[-1]:
                queue.pop()
            queue.append(nums[i])
            if i - left == k-1:
                maxSlidingWindow.append(queue[0])
                if queue[0] == nums[left]:
                    queue.popleft()
                left += 1
        return maxSlidingWindow
        

nums = [1,3,-1,-3,5,3,6,7]
k = 3

print()
print(f"Max sliding window: {Solution.maxSlidingWindow(Solution, nums, k)}")
print()
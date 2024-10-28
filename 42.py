from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft = height[left]
        maxRight = height[right]
        trappedWater = 0

        while left <= right:
            if maxLeft < maxRight:
                if min(maxRight,maxLeft) - height[left] > 0:
                    trappedWater += min(maxRight,maxLeft) - height[left]
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                if min(maxRight, maxLeft) - height[right] > 0:
                    trappedWater += min(maxRight, maxLeft) - height[right]
                maxRight = max(maxRight,height[right])
                right -= 1

        return trappedWater

height = [0,1,0,2,1,0,1,3,2,1,2,1]

print()
print(f"Trapped water: {Solution.trap(Solution, height)}")
print()
from typing import List

class Solution:
    def maxAreaBruteForce(self, height: List[int]) -> int:
        maxWater = 0
        for i in range(len(height)-1):
            j = len(height)-1
            while j > i:
                maxWater = max(maxWater,((j-i)*min(height[i],height[j])))
                j-=1
        return maxWater
    
    def maxAreaOpt(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

height = [1,2,4,3]

print()
print(f"Max amount bruteForce: {Solution.maxAreaBruteForce(Solution, height)}")
print(f"Max amount opt: {Solution.maxAreaOpt(Solution, height)}")
print()
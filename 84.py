from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                max_area = max(heights[index] * (i - stack[-1] - 1 if stack else i), max_area)
            stack.append(i)

        while stack:
            index = stack.pop()
            max_area = max(heights[index] * (len(heights) - stack[-1] - 1 if stack else len(heights)), max_area)

        return max_area

heights = [2,1,5,6,2,3]

print()
print(f"Largest rectangle: {Solution.largestRectangleArea(Solution, heights)}")
print()
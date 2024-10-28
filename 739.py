from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

print()
print(f"Result: {Solution.dailyTemperatures(Solution, temperatures)}")
print()
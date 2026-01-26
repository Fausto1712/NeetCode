from typing import List

class Solution:
    def weirdAlgorithm(self, n: int) -> List[int]:
        values = [n]
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                values.append(n)
            elif n % 2 != 0:
                n = (n * 3) + 1
                values.append(n)
        return values

n = 3

print()
print(f"List of values of n: {Solution.weirdAlgorithm(Solution, n)}")
print()
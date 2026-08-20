from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)
        for spell in spells:
            if spell == 0:
                res.append(0 if success > 0 else n)
                continue
            l, r = 0, n - 1
            ans = n
            while l <= r:
                m = l + (r - l) // 2
                if spell * potions[m] >= success:
                    ans = m
                    r = m - 1
                else:
                    l = m + 1
            res.append(n - ans if ans < n else 0)

        return res


spells = [5,1,3]
potions = [1,2,3,4,5]
success = 7

print()
print(f"Solution: {Solution.successfulPairs(Solution,spells, potions, success)}")
print()
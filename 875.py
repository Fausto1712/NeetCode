from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r =1, max(piles)
        res =  r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            if hours <= h:
                res = min(res,k)
                r = k -1
            else:
                l = k + 1
        return res

piles = [3,6,7,11]

print()
print(f"Result: {Solution.minEatingSpeed(Solution, piles, 8)}")
print()
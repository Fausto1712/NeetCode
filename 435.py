from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        ans = 0
        prev_end = intervals[0][1]

        for s, e in intervals[1:]:
            if s < prev_end:
                ans += 1
            else:
                prev_end = e

        return ans

intervals = [[1,2],[2,3],[3,4],[1,3]]

print()
print(f"Solution: {Solution.eraseOverlapIntervals(Solution,intervals)}")
print()
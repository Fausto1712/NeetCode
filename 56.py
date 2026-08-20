from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for interval in intervals:
            flag = False
            if merged:
                for i in range(len(merged)):
                    if interval[0] <= merged[i][1] and interval[1] >= merged[i][0]:
                        intervals.append([min(merged[i][0], interval[0]), max(merged[i][1], interval[1])])
                        merged = merged[:i] + merged[i+1:]
                        flag = True
                        break
                if not flag:
                    merged.append(interval)
            else:
                merged.append(interval)
        
        return merged

    def merge_sorted(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals = sorted(intervals, key=lambda x: x[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if interval[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)

        return merged


intervals = [[1,3],[2,6],[8,10],[15,18]]

print()
print(f"Solution: {Solution.merge(Solution,intervals)}")
print()
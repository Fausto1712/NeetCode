from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                start = i
                end = i
                
                if intervals[i][0] > newInterval[1]:
                    return intervals[:i] + [newInterval] + intervals[i:]

                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                i += 1
                while i < len(intervals) and intervals[i][0] <= newInterval[1]:
                    newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
                    end = i
                    i += 1
                return intervals[:start] + [newInterval] + intervals[end+1:]

        return intervals + [newInterval]
    
    def insert_sorted(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval = [
                min(newInterval[0], intervals[i][0]),
                max(newInterval[1], intervals[i][1])
            ]
            i += 1

        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result



intervals = [[1,3],[6,9]]
newInterval = [2,5]

print()
print(f"Solution: {Solution.insert(Solution,intervals, newInterval)}")
print()
from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points = sorted(points, key=lambda x:x[0])
        merged = [points[0]]

        for point in points[1:]:
            if point[0] <= merged[-1][1]:
                merged[-1] = [max(merged[-1][0], point[0]), min(merged[-1][1], point[1])]
            else:
                merged.append(point)
        
        return len(merged)
        

points = [[10,16],[2,8],[1,6],[7,12]]

print()
print(f"Solution: {Solution.findMinArrowShots(Solution,points)}")
print()
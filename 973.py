from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []

        for point in points:
            distance = point[0]*point[0] + point[1]*point[1]
            if len(minheap) < k:
                heapq.heappush(minheap, (distance, point))
            elif distance < minheap[0][0]:
                heapq.heapreplace(minheap, (distance, point))
        
        return [point[1] for point in minheap]

points = [[1,3],[-2,2]]
k = 1

print()
print(f"Solution: {Solution.kClosest(Solution,points, k)}")
print()
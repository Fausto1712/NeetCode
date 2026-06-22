from typing import List
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if destination == source:
            return True
        if not edges:
            return False
        adj = {}
        for a, b in edges:
            adj.setdefault(a, []).append(b)
            adj.setdefault(b, []).append(a)

        queue = deque([source])
        visited = {source}

        while queue:
            curr = queue.popleft()
            if curr == destination:
                return True
            for nei in adj.get(curr, []):
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        return False


if __name__ == "__main__":
    solution = Solution()
    n = 5
    edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
    source = 9
    destination = 2

    print(solution.validPath(n, edges, source, destination))
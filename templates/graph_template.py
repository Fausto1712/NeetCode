from __future__ import annotations
from collections import deque
from typing import List, Optional

# Graph template for problems like Clone Graph
# Input example: adjList = [[2,4],[1,3],[2,4],[1,3]]

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"Node({self.val})"


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    if not adj_list:
        return None

    nodes = [Node(i + 1) for i in range(len(adj_list))]
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
    return nodes[0]


def graph_to_adj_list(node: Optional[Node]) -> List[List[int]]:
    if not node:
        return []

    visited = set()
    result: List[List[int]] = []
    queue = deque([node])
    visited.add(node)

    while queue:
        current = queue.popleft()
        while len(result) < current.val:
            result.append([])
        result[current.val - 1] = [neighbor.val for neighbor in current.neighbors]
        for neighbor in current.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        # Replace this stub with your solution.
        return 0


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    original = build_graph(adjList)

    solution = Solution()
    cloned = solution.cloneGraph(original)

    print("Input:", adjList)
    print("Output:", graph_to_adj_list(cloned) if cloned else cloned)
    print("Expected:", [[2, 4], [1, 3], [2, 4], [1, 3]])

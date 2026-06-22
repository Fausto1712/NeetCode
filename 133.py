from __future__ import annotations
from collections import deque
from typing import List, Optional

class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]]=None):
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
    result = []
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
       
       if not node:
           return None
       if not node.neighbors:
           return Node(node.val)
       
       set = {}
       pendingNodes = [node]

       while pendingNodes:
        currNode = pendingNodes.pop()
        if currNode not in set:
            newNode = Node(currNode.val)
            set[currNode] = newNode
        else:
            newNode = set[currNode]

        for neighbor in currNode.neighbors:
            if neighbor not in set:
                createdNeighborNode = Node(neighbor.val)
                set[neighbor] = createdNeighborNode
                pendingNodes.append(neighbor)
                newNode.neighbors.append(createdNeighborNode)
            else:
                newNode.neighbors.append(set[neighbor])
       
       return set[node]


if __name__ == "__main__":
    adjList = []
    original = build_graph(adjList)

    solution = Solution()
    cloned = solution.cloneGraph(original)

    print(graph_to_adj_list(cloned) if cloned else cloned)

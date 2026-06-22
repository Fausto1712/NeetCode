from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(len(edges)+1)]
        visited = {}
        def dfs(curr, prev):
            nonlocal visited
            for connection in graph[curr]:
                if connection != prev:
                    if connection in visited:
                        return False
                    else:
                        visited[curr] = 1
                        if not dfs(connection, curr):
                            return False
                        del visited[curr]
            return True

        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])
            if not dfs(edges[i][0], None):
                return edges[i]
        
if __name__ == "__main__":
    solution = Solution()

    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    print("Result:", solution.findRedundantConnection(edges))
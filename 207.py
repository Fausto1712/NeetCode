from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        requisites = [[] for _ in range(numCourses)]
        mapping = []

        for course, requisite in prerequisites:
            if course == requisite:
                return []
            requisites[course].append(requisite)

        open = {}
        visited = {}

        def dfs(course):
            nonlocal open
            nonlocal visited

            if course in visited:
                return True
            if course in open:
                return False

            open[course] = 1
            for req in requisites[course]:
                if not dfs(req):
                    return False
            del open[course]

            visited[course] = 1
            mapping.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return mapping
        
if __name__ == "__main__":
    solution = Solution()

    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    print("Result:", solution.findOrder(numCourses, prerequisites))
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        requisites = [[] for _ in range(numCourses)]

        for i in range(len(prerequisites)):
            course, requisite = prerequisites[i]
            if course == requisite:
                return False
            requisites[course].append(requisite)

        done = {}
        open = {}
        
        def dfs(course):
            nonlocal done
            nonlocal open

            if course in done:
                return True
            if course in open:
                return False

            if requisites[course]:
                open[course] = 0
                for prerequisite in requisites[course]:
                    if not dfs(prerequisite):
                        return False
                del open[course]
                done[course] = 1
            else:
                done[course] = 1
            return True
        
        for i in range(numCourses - 1, -1, -1):
            if not dfs(i):
                return False
        return True

        
if __name__ == "__main__":
    solution = Solution()

    numCourses = 3
    prerequisites = [[1,0],[1,2],[0,1]]
    print("Result:", solution.canFinish(numCourses, prerequisites))
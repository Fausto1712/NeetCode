from typing import List
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        leastInt = len(tasks)
        taskSet = {}
        heap = []

        for task in tasks:
            taskSet[task] = taskSet.get(task, 0) + 1
        
        for task, count in taskSet.items():
            heapq.heappush(heap, (-count, task))
        
        maxTaskCount = -heap[0][0]
        maxTasks = sum(1 for c in taskSet.values() if c == maxTaskCount)
        possibleMax = ((maxTaskCount-1) * (n+1)) + maxTasks
        return max(leastInt, possibleMax)
    
    def leastIntervalNoHeap(self, tasks: List[str], n: int) -> int:
        leastInt = len(tasks)
        taskSet = {}

        for task in tasks:
            taskSet[task] = taskSet.get(task, 0) + 1
        
        maxTaskCount = max(taskSet.values())
        maxTasks = sum(1 for c in taskSet.values() if c == maxTaskCount)
        possibleMax = ((maxTaskCount-1) * (n+1)) + maxTasks
        return max(leastInt, possibleMax)

tasks = ["A","B","A"]
n = 2

print()
print(f"Solution: {Solution.leastInterval(Solution,tasks, n)}")
print()
from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l1, i = len(firstList), 0
        l2, j = len(secondList), 0
        res = []

        while i < l1 and j < l2:
            if (firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][0]) or (secondList[j][0] <= firstList[i][1] and secondList[j][1] >= firstList[i][0]):
                res.append([max(firstList[i][0],secondList[j][0]), min(firstList[i][1],secondList[j][1])])
            
            if firstList[i][1] <= secondList[j][1]:
                i += 1
            else:
                j += 1
        
        return res

firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

print()
print(f"Solution: {Solution.intervalIntersection(Solution, firstList, secondList)}")
print()
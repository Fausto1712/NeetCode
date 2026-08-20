from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mySet = {}

        for i in range(len(s)):
            if s[i] not in mySet:
                mySet[s[i]] = [i+1]
            else:
                mySet[s[i]].append(i+1)

        res = [1]
        prev = 0
        curr = 1
        for char, pos in mySet.items():
            if pos[0] <= curr:
                if len(res) > 1:
                    res[-1] = max(res[-1], pos[-1] - prev)
                else: 
                    res[-1] = max(res[-1], pos[-1])
                
                curr = max(curr, pos[-1])
            else:
                res.append(pos[-1] - curr)
                prev = curr
                curr = pos[-1]
        
        return res
        

s = "ababcbacadefegdehijhklij"

print()
print(f"Solution: {Solution.partitionLabels(Solution, s)}")
print()
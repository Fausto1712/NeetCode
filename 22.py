from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        p = ""
        def backTrack(open, closed,p):
            if open > n or closed > open:
                return
            if (open + closed) == n * 2:
                res.append(p)
                return
            
            else:
                backTrack(open + 1,closed,p + "(")
                backTrack(open,closed+1,p + ")")

        backTrack(0,0,"")
        return res
print()
print(f"Result: {Solution.generateParenthesis(Solution, 3)}")
print()
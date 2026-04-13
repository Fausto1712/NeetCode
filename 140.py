from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        n = len(s)
        dp = [[False, []] for _ in range(n+1)]
        dp[-1][0] = True
        
        for i in range(n-1, -1,-1):
            for w in wordDict:
                if n - i >= len(w) and w == s[i: i+len(w)]:
                    if not dp[i][0]:
                        dp[i][0] = dp[i+len(w)][0]
                    dp[i][1].append(w)

        res = []
        def dfs(index,solution):
            if index == n:
                res.append(solution[:-1])
                return
            for w in dp[index][1]:
                solution += w + " "
                dfs(index+len(w), solution)
                solution = solution[:len(solution) - (len(w)+1)] 
        
        if dp[0][0]:
            dfs(0,"")

        return res
    
if __name__ == "__main__":
    solution = Solution()

    s = "pineapplepenapple"
    wordDict = ["apple","pen","applepen","pine","pineapple"]
    print(f"Result: {solution.wordBreak(s, wordDict)}")


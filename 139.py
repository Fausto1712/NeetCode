from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        dp = [False] * (n+1)
        dp[-1] = True
        for i in range(n-1,-1,-1):
            for word in wordDict:
                if n - i >= len(word) and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break

        return dp[0]
        
        
    
if __name__ == "__main__":
    solution = Solution()

    s = "leetcode"
    wordDict = ["leet","code"]
    print(f"Result: {solution.wordBreak(s, wordDict)}")


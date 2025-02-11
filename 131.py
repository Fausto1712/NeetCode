from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if is_palindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
        
if __name__ == "__main__":
    solution = Solution()
    s = "aab"
    print(f"The posible palindromes are {solution.partition(s)}")
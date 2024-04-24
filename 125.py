from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        s = s.lower()
        while i < j:
            while i < len(s) and s[i] in "`()!;?-'}{\"[]_#@.,: ":
                i += 1
            while j >= 0 and s[j] in "`()!;?-'}{\"[]_#@.,: ":
                j -= 1  
            if i > len(s)-1:
                return True
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        

str = ".,"

print()
print(f"Solution by brute force: {Solution.isPalindrome(Solution, str)}")
print()
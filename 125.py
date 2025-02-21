from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        s = s.lower()
        
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        

str = "amanaplanacanalpanama"

print()
print(f"Solution by brute force: {Solution.isPalindrome(Solution, str)}")
print()
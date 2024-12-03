class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        charLength = 0
        for i in range(len(s)):
            if s[i] not in charSet:
                charSet.add(s[i])
                charLength += 1
        return charLength
        
string = "abcabcbb"

print()
print(f"The length is: {Solution.lengthOfLongestSubstring(Solution, string)}")
print()
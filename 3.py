class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        charMaxLength = 1
        j = 0
        if len(s) < 1:
            return 0
        for i in range(0, len(s)):
            while s[i] in charSet:
                charSet.remove(s[j])
                j += 1
            charSet.add(s[i])
            charMaxLength = max(charMaxLength, i - j + 1)
        return charMaxLength
        
string = "abcabcbb"

print()
print(f"The length is: {Solution.lengthOfLongestSubstring(Solution, string)}")
print()
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        letterDict = dict()
        i = 0
        maxFreq = 0

        for j in range(len(s)):
            if s[j] not in letterDict:
                letterDict[s[j]] = 0
            letterDict[s[j]] += 1
            maxFreq = max(maxFreq, letterDict[s[j]])
            while j - i + 1 - maxFreq > k:
                letterDict[s[i]] -= 1
                i +=1
            max_length = max(max_length, j - i + 1)

        return max_length

s = "AABABBA"
k = 1

print()
print(f"Longest Repeating Character Replacement: {Solution.characterReplacement(Solution, s, k)}")
print()
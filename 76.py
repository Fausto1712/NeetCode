class Solution:

    def minWindow(self, s: str, t: str) -> str:
        tDict, sDict, left = dict(), dict(), 0
        minWindow = [0, 100000]
        conditionsMet = 0

        for i in range(len(t)):
            if t[i] not in tDict:
                tDict[t[i]] = 0
                sDict[t[i]] = 0
            tDict[t[i]] += 1

        for i in range(len(s)):
            if s[i] in sDict:
                sDict[s[i]] += 1

                if sDict[s[i]] == tDict[s[i]]:
                    conditionsMet += 1

                while conditionsMet == len(tDict):
                    if i + 1 - left < minWindow[1] - minWindow[0]:
                        minWindow = [left, i + 1]
                    if s[left] in sDict:
                        sDict[s[left]] -= 1

                        if sDict[s[left]] < tDict[s[left]]:
                            conditionsMet -= 1

                    left += 1

        if minWindow[1] == 100000:
            return ""
        return s[minWindow[0]:minWindow[1]]


s = 'ADOBECODEBANC'
t = 'ABC'

solution = Solution()
result = solution.minWindow(s, t)
print(f"Longest Repeating Character Replacement: {result}")

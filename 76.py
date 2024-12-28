class Solution:
    def is_dict_subset(dict1, dict2):
        return all(key in dict2 and dict2[key] >= value for key, value in dict1.items())

    def minWindow(self, s: str, t: str) -> str:
        tDict, sDict, left = dict(), dict(), 0
        minWindow = [0,100000]
        for i in range(len(t)):
            if t[i] not in tDict:
                tDict[t[i]] = 0
            tDict[t[i]] +=1
        
        for i in range(len(s)):
            if s[i] not in sDict:
                sDict[s[i]] = 0
            sDict[s[i]] +=1

            while Solution.is_dict_subset(tDict, sDict):
                if i+1 - left < minWindow[1] - minWindow[0]:
                    minWindow = [left, i+1]
                sDict[s[left]] -=1
                if sDict[s[left]] == 0:
                    del sDict[s[left]]
                left += 1
        
        if minWindow[1] == 100000:
            return ""
        return s[minWindow[0]:minWindow[1]]

s = "cabwefgewcwaefgcf"
t = "cae"

print()
print(f"Longest Repeating Character Replacement: {Solution.minWindow(Solution, s, t)}")
print()
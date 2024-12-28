class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict, s2Dict, left = dict(), dict(), 0
        for i in range(len(s1)):
            if s1[i] not in s1Dict:
                s1Dict[s1[i]] = 0
            s1Dict[s1[i]] +=1

        for i in range(len(s2)):
            if s2[i] not in s2Dict:
                s2Dict[s2[i]] = 0
            s2Dict[s2[i]] +=1

            if i - left > len(s1)-1:
                s2Dict[s2[left]] -=1
                if s2Dict[s2[left]] == 0:
                    del s2Dict[s2[left]]
                left += 1
            
            if s1Dict == s2Dict:
                return True
        return False

s1 = "ab"
s2 = "eidbaooo"

print()
print(f"Longest Repeating Character Replacement: {Solution.checkInclusion(Solution, s1, s2)}")
print()
from collections import defaultdict

class Solution:
    """
    Solution with Sorting, sort both String and compare them one by one and return the result
    Time complexity: O(n log n)
    """
    def isAnagramSorting(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t
    
    """
    Solution with HashTable, read both string and for every element in the first add a counter, for every element in the second subtract
    a counter, when both arrays are finished see if all the counters are set to 0, if yes return True, if not return False
    Time complexity: O(n)
    """
    def isAnagramHashTable(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            count = defaultdict(int)
            for i in range(0, len(s)):
                count[s[i]] += 1
                count[t[i]] -= 1

            for val in count.values():
                if val != 0:
                    return False
            return True

string1 = "anagram"
string2 = "nagaram"

print()
print(f"Solution by sorting: {Solution.isAnagramSorting(Solution,string1, string2)}")
print(f"Solution by hashMap: {Solution.isAnagramHashTable(Solution,string1, string2)}")
print()
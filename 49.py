from typing import List
from collections import defaultdict

class Solution:
    """
    Solution with HashTable, iterate through each one of the words and call the isAnagramHashTable for the first value of the 
    grouped anagrams, if the word is an anagram add it to the group, if not continue, if it does not get added create a new,
    group with the word on it
    Time complexity: O(n * m), where n is the total number of characters in all words and m is the number of groups
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
    
    """
    Solution with Sorting and Hash, for every word sort it and use the sorted word as Hash, then append the value to the HashMap
    Time complexity: O(n * k log k), where n is the total number of words and k is the maximum length of a word in the strs list.
    """
    def groupAnagramsSorting(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
        
        return list(anagrams.values())

        
strs = ["eat","tea","tan","ate","nat","bat"]

print()
print(f"Solution by brute force: {Solution.groupAnagrams(Solution, strs)}")
print(f"Solution by brute force: {Solution.groupAnagramsSorting(Solution, strs)}")
print()
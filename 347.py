from collections import defaultdict
from typing import List

class Solution:
    """
    Solution with HashTable and sort, first we create a hash table with all the occurrences of each number as the value and the key
    as the actual number, the we sort said hash and slice the k first numbers, then we create an array using the numbers and
    return it
    Time complexity: O(n + k), where n is the total number of numbers and k the required number of most elements
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        k_highest = sorted(count.items(), key=lambda x: x[1], reverse=True)[:k]
        k_highest_keys = [item[0] for item in k_highest]

        return k_highest_keys

nums = [4,4,7,7,7,8,10,5,3]
k = 2

print()
print(f"Solution by hashmap: {Solution.topKFrequent(Solution,nums, k)}")
print()
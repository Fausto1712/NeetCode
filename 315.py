from enum import Enum
from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        enum = list(enumerate(nums))
        def mergeSort(enum,l,r):
            if l >= r:
                return
            
            m = l + (r - l) // 2
            mergeSort(enum, l, m)
            mergeSort(enum, m + 1, r)
            merge(enum, l, m, r)

        def merge(enum,l,m,r):
            i, j = l , m+1
            temp = []
            inversion = 0
            while i < m+1 and j < r+1:
                if enum[i][1] <= enum[j][1]:
                    temp.append(enum[i])
                    res[enum[i][0]] += inversion
                    i += 1
                else:
                    temp.append(enum[j])
                    inversion += 1
                    j += 1
            
            while i < m+1:
                temp.append(enum[i])
                res[enum[i][0]] += inversion
                i += 1
            while j < r+1:
                temp.append(enum[j])
                inversion += 1
                j += 1
            enum[l:r+1] = temp
        
        mergeSort(enum, 0, len(nums)-1)
        return res



if __name__ == "__main__":
    solution = Solution()
    nums = [5,2,6,1]
    print(f"The solution is are: {solution.countSmaller(nums)}")
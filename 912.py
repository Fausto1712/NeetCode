from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(array, left, right):
            if left >= right:
                return
            
            mid = left + (right - left) // 2
            mergeSort(array, left, mid)
            mergeSort(array, mid + 1, right)
            merge(array, left, mid, right)

        def merge(array, left, mid, right):
            left_part = array[left:mid + 1]
            right_part = array[mid + 1:right + 1]

            i = j = 0
            k = left
            
            while i < len(left_part) and j < len(right_part):
                if left_part[i] <= right_part[j]:
                    array[k] = left_part[i]
                    i += 1
                else:
                    array[k] = right_part[j]
                    j += 1
                k += 1
            
            while i < len(left_part):
                array[k] = left_part[i]
                i += 1
                k += 1
                
            while j < len(right_part):
                array[k] = right_part[j]
                j += 1
                k += 1

        nums_copy = nums.copy()
        mergeSort(nums_copy, 0, len(nums_copy) - 1)
        return nums_copy


if __name__ == "__main__":
    solution = Solution()
    nums = [5,2,3,1,7]
    print(f"The possible arrangements are: {solution.sortArray(nums)}")
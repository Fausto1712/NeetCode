from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = 1
        haveZero = 0
        answer = []
        for num in nums:
            if num != 0:
                result = result * num
            else:
                haveZero += 1
        for num in nums:
            if haveZero >= 2:
                answer.append(0)
            elif (haveZero == 1) and (num == 0):
                answer.append(result)
            elif haveZero == 1:
                answer.append(0)
            else:
                answer.append(int(result/num))
        return answer

nums = [1,2,3,4]

print()
print(f"Solution: {Solution.productExceptSelf(Solution, nums)}")
print()
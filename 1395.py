from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cache = {}

        def backtrack(i, ascend, count):
            key = (i, ascend, count)
            if key in cache:
                return cache[key]

            if count == 3:
                return 1

            if i == len(rating):
                return 0

            res = 0
            for j in range(i + 1, len(rating)):
                if ascend and rating[i] < rating[j]:
                    res += backtrack(j, ascend, count + 1)
                if not ascend and rating[i] > rating[j]:
                    res += backtrack(j, ascend, count + 1)

            cache[key] = res
            return res

        res = 0
        for i in range(len(rating)):
            res += backtrack(i, True, 1)
            res += backtrack(i, False, 1)
        return res

    def numTeamsOpt(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        for j in range(n):
            left_smaller = 0
            left_greater = 0
            right_smaller = 0
            right_greater = 0

            for i in range(j):
                if rating[i] < rating[j]:
                    left_smaller += 1
                else:
                    left_greater += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_smaller += 1
                else:
                    right_greater += 1

            res += left_smaller * right_greater
            res += left_greater * right_smaller

        return res
    
if __name__ == "__main__":
    solution = Solution()

    rating = [2,5,3,4,1]
    print(f"Result: {solution.numTeams(rating)}")
    print(f"Result Opt: {solution.numTeamsOpt(rating)}")


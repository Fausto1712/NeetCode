from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        index = {v: i for i, v in enumerate(arr)}
        dp = [[0] * n for _ in range(n)]
        maximum = 0

        for i in range(n):
            for j in range(i - 1, -1, -1):
                diff = arr[i] - arr[j]
                if diff >= arr[j]:
                    break
                if diff in index:
                    k = index[diff]
                    dp[j][i] = (dp[k][j] or 2) + 1
                    if dp[j][i] > maximum:
                        maximum = dp[j][i]

        return maximum if maximum >= 3 else 0

if __name__ == "__main__":
    solution = Solution()
    arr = [2,4,7,8,9,10,14,15,18,23,32,50]

    print(f"Result: {solution.lenLongestFibSubseq(arr)}")

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = {}

        def dfs(i, m, n):
            if i == len(strs):
                return 0
            
            if (i, m, n) in dp:
                return dp[(i,m,n)]
            
            x=0
            y=0
            for char in strs[i]:
                if char == "0":
                    x += 1
                else:
                    y += 1

            if m-x >= 0 and n-y >= 0:
                dp[(i,m,n)] = max(dfs(i+1,m-x,n-y)+1, dfs(i+1,m,n))
            else:
                dp[(i,m,n)] = dfs(i+1,m,n)

            return dp[(i,m,n)]
        return dfs(0, m, n)
    
if __name__ == "__main__":
    solution = Solution()

    strs = ["01111111111111111111111111","10111111111111111111111111","11011111111111111111111111","11101111111111111111111111","11110111111111111111111111","11111011111111111111111111","11111101111111111111111111","11111110111111111111111111","11111111011111111111111111","11111111111111111111111110","001111111111","111111111100","00001100","00110000"]
    m = 8
    n = 9
    print(f"Result: {solution.findMaxForm(strs, m,n)}")


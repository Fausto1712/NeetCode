from typing import List
class Solution:
    def countingBites(self, characters) -> str:
        res = ""
        count = 1

        for i in range(len(characters)-1):
            if characters[i] != characters[i+1]:
                res =  res + characters[i] + str(count)
                count = 1
            else:
                count += 1
        res =  res + characters[-1] + str(count)
        return res

if __name__ == "__main__":
    solution = Solution()
    print(f"The solution is {solution.countingBites(["a","a","a","a","a","b","b","b","c","c","c","c"])}")
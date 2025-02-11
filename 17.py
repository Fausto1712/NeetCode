from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 1:
            return []
        
        res = []
        numberToLetters = {
            "2": ["a","b","c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r","s"],
            "8": ["t","u","v"],
            "9": ["w","x","y","z"]
        }

        def dfs(index, combination):
            if index == len(digits):
                res.append(combination)
                return
            
            for letter in numberToLetters[digits[index]]:
                combination += letter
                dfs(index+1, combination)
                combination = combination[:-1]

        dfs(0, "")
        return res

if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    print(f"The viable combinatios are: {solution.letterCombinations(digits)}")
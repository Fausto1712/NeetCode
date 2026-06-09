class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxV = 0
        """ vowels = {"a","e","i","o","u"}"""
        vowels = set("aeiou")

        for char in range(k):
            if s[char] in vowels:
                maxV += 1
        curr = maxV

        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i-k] in vowels:
                curr -= 1
            maxV = max(maxV, curr)
        
        return maxV
    
if __name__ == "__main__":
    solution = Solution()

    s = "tryhard"
    k = 4
    print(f"Result: {solution.maxVowels(s, k)}")


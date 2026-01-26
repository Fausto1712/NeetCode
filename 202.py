class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n: int) -> int:
        output = 0
        
        while n:
            digit = (n % 10) ** 2
            output += digit 
            digit = (n / 10) ** 2
            n = n // 10

        return output


n = 19
solution = Solution()

print()
print(f"The number is {'not ' if not solution.isHappy(n) else ''}happy")
print()
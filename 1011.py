from typing import List

class Solution:
    """
    Brute Force Solution: Try every possible capacity from max(weights) to sum(weights)
    Time complexity: O(n * sum(weights))
    Space complexity: O(1)
    This approach would be inefficient for large inputs
    """
    def shipWithinDaysBruteForce(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            current_weight = 0
            days_needed = 1
            
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight
            
            return days_needed <= days

        for capacity in range(max(weights), sum(weights) + 1):
            if canShip(capacity):
                return capacity
        
        return sum(weights)
    
    """
    Optimal Binary Search Solution: Use binary search on the answer space
    The key insight is that if we can ship with capacity X, we can also ship with capacity X+1
    This monotonic property allows us to use binary search
    Time complexity: O(n * log(sum(weights)))
    Space complexity: O(1)
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            current_weight = 0
            days_needed = 1
            
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = weight
                    if days_needed > days:
                        return False
                else:
                    current_weight += weight
            
            return True
        

        left = max(weights)
        right = sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValid(mid):
            sum = 0
            daysCount = 1
            for i in range (n):
                sum += weights[i]
                if sum > mid:
                    daysCount += 1
                    sum = weights[i]
                    if daysCount > days:
                        return False
            return True

        n = len(weights)
        right = sum(weights)
        left = max(weights)
        while left < right:
            mid = (left+right)//2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        mid = (left+right)//2
        return mid




if __name__ == "__main__":
    solution = Solution()
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    
    print(f"Brute Force Solution: {solution.shipWithinDaysBruteForce(weights, days)}")
    print(f"Optimal Binary Search Solution: {solution.shipWithinDays(weights, days)}")

from typing import List
import heapq

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        
        if self.maxHeap and self.minHeap and (-self.maxHeap[0] > self.minHeap[0]):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return float(-self.maxHeap[0])
        return (-self.maxHeap[0] + self.minHeap[0]) / 2.0


if __name__ == "__main__":
    # Test case 1: Basic functionality
    print("Test case 1: Basic functionality")
    mf = MedianFinder()
    mf.addNum(1)
    print(f"After adding 1: {mf.findMedian()}")  # Expected: 1.0
    
    mf.addNum(2)
    print(f"After adding 2: {mf.findMedian()}")  # Expected: 1.5
    
    mf.addNum(3)
    print(f"After adding 3: {mf.findMedian()}")  # Expected: 2.0
    
    print()
    
    # Test case 2: Negative numbers
    print("Test case 2: Negative numbers")
    mf2 = MedianFinder()
    mf2.addNum(-1)
    print(f"After adding -1: {mf2.findMedian()}")  # Expected: -1.0
    
    mf2.addNum(0)
    print(f"After adding 0: {mf2.findMedian()}")  # Expected: -0.5
    
    mf2.addNum(1)
    print(f"After adding 1: {mf2.findMedian()}")  # Expected: 0.0
    
    print()
    
    # Test case 3: Even and odd counts
    print("Test case 3: Even and odd counts")
    mf3 = MedianFinder()
    nums = [5, 15, 1, 3, 8]
    for num in nums:
        mf3.addNum(num)
        print(f"After adding {num}: median = {mf3.findMedian()}")
    
    print()
    
    # Test case 4: Duplicate numbers
    print("Test case 4: Duplicate numbers")
    mf4 = MedianFinder()
    for num in [2, 2, 2, 2]:
        mf4.addNum(num)
        print(f"After adding {num}: median = {mf4.findMedian()}")
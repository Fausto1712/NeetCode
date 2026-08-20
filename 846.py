from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()

        while hand:
            prev = hand.pop()
            count = 1
            skipped = []

            while count < groupSize:
                if not hand:
                    return False

                if hand[-1] == prev:
                    skipped.append(hand.pop())
                    continue

                if hand[-1] != prev - 1:
                    return False

                prev = hand.pop()
                count += 1

            if skipped:
                hand.extend(reversed(skipped))

        return True
                
        

hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3

print()
print(f"Solution: {Solution.isNStraightHand(Solution, hand, groupSize)}")
print()
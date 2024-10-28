from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        carFleets = 0
        prev_time = 0
        
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > prev_time:
                carFleets += 1
                prev_time = time
                
        return carFleets

target = 10
position = [0, 4, 2]
speed = [2, 1, 3]

print()
print(f"Number of car fleets: {Solution.carFleet(Solution, target, position, speed)}")
print()
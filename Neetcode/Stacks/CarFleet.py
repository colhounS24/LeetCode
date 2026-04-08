
from typing import List
# Space complexity is O(n), so I would imagine that you could have a stack for each car in the array, and if the stacks are the same height and now equal to the target, add

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        arrival_times = []
        pairs = sorted(zip(position, speed), reverse=True)

        for pos, s in pairs:
           arrival_times.append((target-pos)/s)

        fleets = []
        for time in arrival_times:
            if len(fleets) == 0:
                fleets.append(time)
            elif fleets[-1] < time:
                fleets.append(time)

        return len(fleets)

                

        




        
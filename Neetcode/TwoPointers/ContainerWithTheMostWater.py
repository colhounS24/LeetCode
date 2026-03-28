from typing import List

# Given an array of heights

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lh_pointer = 0
        rh_pointer = len(heights) - 1
        max_volume = 0
        

        while lh_pointer < rh_pointer:
            volume = (rh_pointer - lh_pointer) * min(heights[lh_pointer], heights[rh_pointer])

            if volume > max_volume:
                max_volume = volume

            if heights[lh_pointer] < heights[rh_pointer]:
                lh_pointer += 1

            elif heights[lh_pointer] > heights[rh_pointer]:
                rh_pointer -= 1

            else:
                lh_pointer += 1
                rh_pointer -= 1

        return max_volume

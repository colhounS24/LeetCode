# Given: an integer array piles, where piles[i] is the nimber of bananas in the ith pile
# Given: an integer h which is the number of hours to eat all of the bananas

# Action: you decide the bananas per hour, k
# Action: Each iteration, eat k bananas from a pile, if less than k bananas in a pile, you eat the remainder

# Return: the minimuim k s.t. you can eat all bananas in h hrs

# Target: Eat all of the bananas


# It takes ceil(x/k) to eat a pile of x bananas at a rate k
# worst case scenario for k is max(piles)
# 1<= k <= max(piles)

import math

class Solution:
    @staticmethod
    def _canIEatAll(arr, rate, target):
        total_time = 0
        for a in arr:
            total_time += math.ceil(a / rate)
        if total_time <= target:
            return True
        else:
            return False

    @staticmethod
    def _binarySearch(arr, h):
        a = 1
        b = max(arr)

        while a <= b:
            mid = ((a+b) // 2)
            
            # If you can do it, try to reduce it 
            if Solution._canIEatAll(arr, mid, h):
                b = mid -1
            else:
            # Couldn't do it
                a = mid + 1

        return a

        


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
       return self._binarySearch(piles, h)

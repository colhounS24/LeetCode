from typing import  List
# [1,2,3,4]
# [3,4,5,6,1,2] -- find min

# 2 pointers, LH and RH
# Case 1: arr[mid] is < arr[RH] --> min in LHS, thus RH = mid - 1
# Case 2: arr[mid] is > arr[RH] --> min in RHS, thus RH = mid + 1
# stop when RH == LH, this is the min

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lh = 0
        rh = len(nums) - 1

        while lh < rh:
            mid = (lh + rh) // 2

            # Case 1
            if nums[mid] < nums[rh]:
                rh = mid
            # Case 2
            elif nums[mid] > nums[rh]:
                lh = mid + 1
            
        return nums[lh]
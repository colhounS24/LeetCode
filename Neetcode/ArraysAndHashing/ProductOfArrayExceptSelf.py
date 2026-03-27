from typing import List

# Brute force soltn
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # Initialise the result array to be all 1's

        prefix = 1 # settign the LHS prefix to 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums)-1,-1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
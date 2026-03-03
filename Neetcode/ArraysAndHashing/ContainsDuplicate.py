"""
Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false


"""
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_nums = set()

        for i in range(len(nums)):
            if nums[i] in checked_nums:
                return True
            else:
                checked_nums.add(nums[i])
        return False
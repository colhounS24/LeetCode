class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in indexes:
                return sorted([i, indexes[complement]])
            indexes[num] = i


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lh = 0
        rh = len(nums) - 1

        while lh < rh:
            mid = (lh + rh) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] < nums[rh]:
                if target > nums[mid] and target <= nums[rh]:
                    lh = mid + 1
                else:
                    rh = mid - 1
            else:
                if target >= nums[lh] and target < nums[mid]:
                    rh = mid -1
                else:
                    lh = mid + 1
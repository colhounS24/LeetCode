class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lh_pointer = 0 # start
        rh_pointer = len(numbers) - 1 # end

        while lh_pointer < rh_pointer:
            if numbers[lh_pointer] + numbers[rh_pointer] > target:
                rh_pointer -= 1
            elif numbers[lh_pointer] + numbers[rh_pointer] < target:
                lh_pointer += 1
            else:
                return [lh_pointer +1, rh_pointer + 1]
class Solution:

    @staticmethod
    def twoSum(nums: List[int], start: int, target: int) -> List[int]:
        # sorted list being passed in
        lh_pointer = start
        rh_pointer = len(nums) - 1
        res = []
        while lh_pointer < rh_pointer:
            if nums[lh_pointer] + nums[rh_pointer] > target:
                rh_pointer -= 1
            elif nums[lh_pointer] + nums[rh_pointer] < target:
                lh_pointer += 1
            else: # Success
                res.append([nums[lh_pointer], nums[rh_pointer]])
                lh_pointer += 1
                
                while lh_pointer < rh_pointer and nums[lh_pointer] == nums[lh_pointer - 1]:
                    lh_pointer += 1
                rh_pointer -= 1
                
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sprt it in place
        
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            
            result = self.twoSum(nums, i + 1, target)
            if result:
                for pair in result:
                    res.append([nums[i]] + pair)


        return res

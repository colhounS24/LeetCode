class Solution:
    def search(self, nums: list[int], target: int) -> int:
        a = 0
        b = len(nums) - 1 # take 1  off because of indexing

        while a <= b: # This works because we are looking to do this whilst they are not equal, if they are equal, that is opur value
            mid = ((b-a) //2) + a 
            if nums[mid] < target:
                a = mid + 1
            elif nums[mid] > target:
                b = mid - 1
            else:
                return mid
        return -1

solution = Solution()
print(solution.search([1,3,5,7,9], 7))